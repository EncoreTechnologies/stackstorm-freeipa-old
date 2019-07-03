#!/usr/bin/env python
import argparse
import git
import jinja2
import os
import shutil
import yaml


GIT_DIR = './freeipa'
GIT_URL = 'https://github.com/freeipa/freeipa.git'

ACTION_TEMPLATE_PATH = "./templates/action.yaml.j2"
ACTION_DIRECTORY = "../actions"
PYTHON_TEMPLATE_PATH = "./templates/ipa_command_args_options.py.j2"
IPA_RELEASE_TAG_PREFIX = "release-"

API_SPEC_DIR = './specs'

VIRTUALENV_DIR = './virtualenv'

IPA_TYPE_TO_STACKSTORM_TYPE = {
    "A6Record": "string",
    "AAAARecord": "string",
    "AFSDBRecord": "string",
    "APLRecord": "string",
    "ARecord": "string",
    "Bool": "boolean",
    "Bytes": "string",
    "CERTRecord": "string",
    "CNAMERecord": "string",
    "Certificate": "string",
    "CertificateSigningRequest": "string",
    "DHCIDRecord": "string",
    "DLVRecord": "string",
    "DNAMERecord": "string",
    "DNOrURL": "string",
    "DNParam": "string",
    "DNSNameParam": "string",
    "DSRecord": "string",
    "DateTime": "string",
    "Decimal": "number",
    "Dict": "object",
    "Entry": None,
    "Flag": "boolean",
    "HIPRecord": "string",
    "IA5Str": "string",
    "IPSECKEYRecord": "string",
    "Int": "integer",
    "IntEnum": "integer",
    "KEYRecord": "string",
    "KXRecord": "string",
    "LOCRecord": "string",
    "ListOfEntries": None,
    "ListOfPrimaryKeys": None,
    "MXRecord": "string",
    "NAPTRRecord": "string",
    "NSECRecord": "string",
    "NSRecord": "string",
    "OTPTokenKey": "string",
    "Output": None,
    "PTRRecord": "string",
    "Password": "string",
    "PrimaryKey": "string",
    "Principal": "string",
    "RPRecord": "string",
    "RRSIGRecord": "string",
    "SIGRecord": "string",
    "SPFRecord": "string",
    "SRVRecord": "string",
    "SSHFPRecord": "string",
    "Str": "string",
    "StrEnum": "string",
    "TLSARecord": "string",
    "TXTRecord": "string",
    "URIRecord": "string",
}

IPA_METHOD_LOGIN = {
    'name': 'login',
    'parameters': [],
    'args': [],
    'options': [],
    'outputs': [],
}


def to_yaml_string(value, indent=None, allow_unicode=True):
    options = {'default_flow_style': False}
    if indent is not None:
        options['indent'] = indent
    if allow_unicode is not None:
        options['allow_unicode'] = allow_unicode
    return yaml.safe_dump(value, **options)


class Cli:
    def parse(self):
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        # Subparsers
        subparsers = parser.add_subparsers(dest="command")

        # fetch-spec
        subparsers.add_parser('fetch-spec',
                              help="Clone freeipa git repo and grab the latest API spec.")

        # generate
        generate_parser = subparsers.add_parser('generate',
                                                help="Generate actions from an API spec.")
        generate_parser.add_argument('-d', '--directory', default=ACTION_DIRECTORY,
                                     help=("Directory where actions should be written\n"
                                           "  (default: %(default)s)"))

        default_spec = None
        if os.path.exists(API_SPEC_DIR):
            spec_files = sorted(os.listdir(API_SPEC_DIR))
            if spec_files:
                default_spec = os.path.join(API_SPEC_DIR, spec_files[-1])
        generate_parser.add_argument('-s', '--spec', default=default_spec,
                                     help=("API spec file to use, should be a file in specs/"
                                           " (default: %(default)s)"))

        subparsers.add_parser('examples',
                              help="Prints examples of how to use this script to stdout")

        args = parser.parse_args()
        if args.command == "examples":
            self.examples()
            exit(0)
        return args

    def examples(self):
        print("# fetch the latest API spec from the freeipa git repo/\n"
              "./action_generate.py fetch-spec\n"
              "\n"
              "# gerenate actions from the latest API spec/\n"
              "./action_generate.py generate\n"
              "\n"
              "# gerenate actions into an alternate directory from the latest API spec/\n"
              "./action_generate.py generate -d ../actions_new\n"
              "\n"
              "# gerenate actions from a specific API spec/\n"
              "./action_generate.py generate -s ./specs/API-release-1.2.3.txt\n")


class IpaGitRepo(object):

    def __init__(self, dirname, git_url):
        self.dirname = dirname
        self.git_url = git_url

    def clone(self):
        # pull the repo, if it exists, or clone if it doesn't exist
        if os.path.exists(self.dirname):
            self.repo = git.Repo(self.dirname)
            remote = self.repo.remote()
            self.repo.git.checkout('master')
            remote.pull()
        else:
            self.repo = git.Repo.clone_from(self.git_url, self.dirname)

    def get_latest_release(self):
        # find all tags on the repo that start with "release-"
        release_tags = []
        for t in self.repo.tags:
            if t.name.startswith(IPA_RELEASE_TAG_PREFIX):
                release_tags.append(t.name)

        if len(release_tags) <= 0:
            print("ERROR: Coulnd't find any tags in the freeipa/ repo that start with: \"{}\""
                  .format(IPA_RELEASE_TAG_PREFIX))
            exit(1)

        # find latest release, by version number
        release_tags = sorted(release_tags)
        self.latest_release = release_tags[-1]

        return self.latest_release

    def clone_latest_release(self):
        self.clone()
        latest_release = self.get_latest_release()

        # checkout the latest release tag
        self.repo.git.checkout(latest_release)

        return latest_release

    def copy_api_txt(self, dst):
        if not os.path.exists(API_SPEC_DIR):
            os.mkdir(API_SPEC_DIR)
        src = os.path.join(self.dirname, 'API.txt')
        dst = os.path.join(dst, 'API-{}.txt'.format(self.latest_release))
        shutil.copyfile(src, dst)
        return dst


class IpaType(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class IpaApiParser(object):

    def parse(self, filename):
        self.type_names = set()
        method_list = []
        # the login method isn't in the API.txt file, but we need it
        # to create a persistent session over multiple commands
        method_list.append(IPA_METHOD_LOGIN)
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
            method = {}
            for l in lines:
                if l.startswith('command: '):
                    full_command = l.split('command: ')[1]
                    command, version = full_command.split('/')
                    if method:
                        method_list.append(method)
                    method = self.make_method(command, version)
                elif l.startswith('args: '):
                    pass
                    # full_args = l.split('args: ')[1]
                    # num_args, num_options, num_output = full_args.split(',')
                    # method['num_args'] = int(num_args)
                    # method['num_options'] = int(num_options)
                    # method['num_output'] = int(num_output)
                elif l.startswith('arg: '):
                    arg = l.split('arg: ')[1]
                    type_info = self.parse_datatype(arg)
                    method['args'].append(type_info)
                    method['parameters'].append(type_info)
                elif l.startswith('option: '):
                    option = l.split('option: ')[1]
                    type_info = self.parse_datatype(option)
                    method['options'].append(type_info)
                    method['parameters'].append(type_info)
                # # ignore output lines until we support output schema on actions
                # elif l.startswith('output: '):
                    # output = l.split('output: ')[1]
                    # method['outputs'].append(self.parse_output(output))
        return method_list

    def make_method(self, command, version):
        return {
            'name': command,
            'version': int(version),
            'parameters': [],
            'args': [],
            'options': [],
            'outputs': [],
        }

    def parse_datatype(self, datatype):
        data_parts = datatype.split('(')
        ipa_type_name = data_parts[0]
        ipa_type_data = data_parts[1]
        custom_type_python = "IpaType({}".format(ipa_type_data)
        type_info = {}
        type_info['type'] = IPA_TYPE_TO_STACKSTORM_TYPE[ipa_type_name]
        type_info['required'] = False

        try:
            custom_type = eval(custom_type_python)
            type_info['name'] = custom_type.args[0]
            if len(custom_type.args) != 1:
                raise ValueError("len(args) != 1 - datatype='{}' len(args)={}".
                                 format(datatype, len(custom_type.args)))

            if custom_type.kwargs.get('autofill', False):
                type_info['required'] = True
            if 'default' in custom_type.kwargs:
                type_info['default'] = custom_type.kwargs['default']
            # handle string enums (ignore int enums because StackStorm doesn't handle them)
            if 'values' in custom_type.kwargs and ipa_type_name == 'StrEnum':
                type_info['enum'] = custom_type.kwargs['values']

        except SyntaxError:
            # if doing the eval(custom_type_python) fails because of bad syntax they have
            #  then just pull out the name of the parameter as the first string from
            #  the data type itself
            data_parts = ipa_type_data.split(',')
            type_info['name'] = data_parts[0].replace("'", '')
            pass

        # remove ? from type names
        if '?' in type_info['name']:
            type_info['name'] = type_info['name'].replace('?', '')
        if '+' in type_info['name']:
            type_info['name'] = type_info['name'].replace('+', '')
            type_info['required'] = True
        if '*' in type_info['name']:
            type_info['name'] = type_info['name'].replace('*', '')
            type_info['array_items'] = {'type': type_info['type']}
            type_info['type'] = 'array'

        if ipa_type_name == 'Password':
            type_info['secret'] = True

        return type_info


class St2ActionGenerator(object):

    def create_template(self, template_filename):
        path, filename = os.path.split(template_filename)
        environment = jinja2.Environment(loader=jinja2.FileSystemLoader(path or './'))
        environment.filters['to_yaml_string'] = to_yaml_string
        return environment.get_template(filename)

    def generate_actions(self, action_list, action_dir):
        template = self.create_template(ACTION_TEMPLATE_PATH)
        for action in action_list:
            action_data = template.render(action)
            action_filename = "{}/{}.yaml".format(action_dir, action['name'])
            with open(action_filename, "w") as f:
                f.write(action_data)

    def generate_python_file(self, action_list, action_dir):
        template = self.create_template(PYTHON_TEMPLATE_PATH)
        python_data = template.render({'actions': action_list})
        python_filename = "{}/{}.py".format(action_dir, 'ipa_command_args_options')
        with open(python_filename, "w") as f:
            f.write(python_data)


def clean_temp_dirs():
    shutil.rmtree(GIT_DIR)
    shutil.rmtree(VIRTUALENV_DIR)


if __name__ == "__main__":
    cli = Cli()
    args = cli.parse()
    if args.command == 'fetch-spec':
        # get the latest release from git and copy the API spec from that release
        repo = IpaGitRepo(GIT_DIR, GIT_URL)
        repo.clone_latest_release()
        api_spec_file = repo.copy_api_txt(API_SPEC_DIR)
        print(api_spec_file)
    elif args.command == 'generate':
        # parse the API spec
        parser = IpaApiParser()
        actions = parser.parse(args.spec)

        # generate actions and python from the API spec
        generator = St2ActionGenerator()
        generator.generate_actions(actions, args.directory)
        generator.generate_python_file(actions, args.directory)
    elif args.command == 'clean':
        clean_temp_dirs()
    else:
        raise ValueError("CLI Error: Unknown command = {}".format(args.command))
