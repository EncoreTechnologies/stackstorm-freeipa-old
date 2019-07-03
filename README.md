[![Build Status](https://circleci.com/gh/EncoreTechnologies/stackstorm-freeipa.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/EncoreTechnologies/stackstorm-freeipa) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# FreeIPA Integration Pack

# <a name="Introduction"></a> Introduction
This pack provides integration with the FreeIPA API (https://www.freeipa.org/)
Actions within this pack mirror one-for-one the "Commands" in the API (https://github.com/freeipa/freeipa/blob/master/API.txt).
Data types and payloads also mirror one-for-one.

# <a name="QuickStart"></a> Quick Start
1. Currently this pack is in incubation, so installation must be performed from the github page:
  ``` shell
  st2 pack install https://github.com/EncoreTechnologies/stackstorm-freeipa.git
  ```
2. Execute an action (example: add a new host)
  ``` shell
  st2 run freeipa.host_add server=ipaserver.domain.tld user=administrator password=xxx
```
# <a name="Configuration"></a> Configuration

## <a name="Schema"></a> Schema

``` yaml
---
connections:
  <credential-name-1>:
    server: <hostname or ip of the IPA server>
    user: <username@domain.tld (preferred) or domain\username>
    password: <password for username>
  <credential-name-2>:
    server: <hostname or ip of the IPA server>
    user: <username@domain.tld (preferred) or domain\username>
    password: <password for username>
  <connection-name-3>:
    ... # note: multiple connections can be specified!
```

## <a name="SchemaExample"></a> Schema Example
``` yaml
---
connections:
  # note: if no 'connection' parameter is specified, then the 'default' connection
  # from the pack config will be used
  default:
    user: "userexample"
    password: "passwordexample"
    server: "serverexample"
  test:
    user: ipaadminuser
    password: super secret
    server: same thing as hostname
```

**Note** : All actions allow you to specify a set of credentials as inputs
           to the action instead of requiring a configuration. See the [Actions](#Actions)
           section for more information.

# <a name="Actions"></a> Actions
Actions in this pack are auto-generated based on an API specfication file located in 
`etc/spec/API-release-*.txt`. The specification file is the `API.txt` file in the
[freeipa git repository](https://github.com/freeipa/freeipa). We then use that `API.txt`
file to auto-generate all of our actions using the script `etc/generate_actions.py`.
Each `command` in the API.txt generates a new action YAML file.
FreeIPA commands are parsed and all `args` and `options` are added in as action parameters
using their native StackStorm data types.

## <a name="Usage"></a> Usage

### <a name="BasicUsage"></a> Usage - Basic

Actions created mirror the FreeIPA API, so passing in arguments and options 

``` shell
st2 run freeipa.host_add fqdn='hostname.domain.tld' all=true
st2 run freeipa.host_del fqdn='hostname.domain.tld' all=true
st2 run freeipa.hostgroup_add_member cn='nameofhostgroup' all=true host=['hostname.domain.tld']
```

The following example demonstrates running the `freeipa.host_add` action using action input parameters.

``` shell
$ st2 run freeipa.host_add fqdn='ipahostname.domain.tld all=true
..
id: 59722f939900aa7b61ca9983
status: succeeded
parameters:
  fqdn: ipahostname.domain.tld
  all: True
result:
  exit_code: 0
  result:
    error:
      code: 4002
      data: {}
      message: host with name "ipahostname.domain.tld" already exists
      name: DuplicateEntry
    id: 0
    principal: administrator@IPASERVER.DOMAIN.TLD
    result: null
    version: 4.4.0
  stderr: ''
  stdout: ''
```

### <a name="UsageConfig"></a> Usage - Config Connection

This pack is designed to store commonly used connection information in the pack's
config file located in `/opt/stackstorm/config/freeipa.yaml`. The connection 
info is specified in the config once, and then referenced by name within an
action and/or workflow. 

Using the action from the basic example, we can enter this connection information
in our config:

``` shell
$ cat /opt/stackstorm/configs/freeipa.yaml
---
connections:
  prod:
    server: freeipa.domain.tld
    user: administrator
    password: xxx
```

Now we can reference this connection (by name) when executing our action:

``` shell
$ st2 run freeipa.login connection=prod
```

This pays off big time when running multiple commands in sequence.


### <a name="UsageConfig"></a> Usage - Config Connection Default

To avoid repeated typing of the `connection` parameter this pack also supports
the concept of a `default` connection. Simply specify a connection in the pack
config with the name `default` and this connection will be used for all commands.


``` shell
$ cat /opt/stackstorm/configs/freeipa.yaml
---
connections:
  default:
    server: freeipa.domain.tld
    user: administrator
    password: xxx
```

Now we can omit the `connection` option when running our actions and the `default` connection will be used:

``` shell
$ st2 run freeipa.login
```


### <a name="UsageLogin"></a> Usage - Login Sessions

By default this pack performs a login operation in every action if the `session` 
parameter is not passed in. To avoid these repetitive logins under the hood
we can perform the login operation and then re-use the login session cookie
in all subsequent actions

There are 2 ways you can use this feature as explained above:

1. Config
```
$ st2 run freeipa.login connection=prod
....
id: 598c977da2fb38cf298a28f9
status: succeeded
parameters:
  connection: abc
result:
  exit_code: 0
  result: MagBearerToken=abcdef
  stderr: 'st2.actions.python.login: INFO     Successfully logged in as administrator

    '
  stdout: ''
```

2. Basic
```
$ st2 run freeipa.login server=ipaserver.domain.tld user=administrator password=xxx
....
id: 598c977da2fb38cf298a28f9
status: succeeded
parameters:
  connection: abc
result:
  exit_code: 0
  result: MagBearerToken=abcdef
  stderr: 'st2.actions.python.login: INFO     Successfully logged in as administrator

    '
  stdout: ''
```

Both options return a string for the cached session cookie that is then passed into the next actions
the user invokes in the "session" parameter for example:

``` shell
st2 run freeipa.host_add session='MagBearerToken=abcdef' args=ipahostname.domain.tld params=['all':True,'force':True]'
...
id: 598dcac0a2fb38cf298a2983
status: succeeded
parameters:
  args:
  - ipahostname.domain.tld
  params: {}
  server: ipahostname.domain.tld
  session: MagBearerToken=abcdef
result:
  exit_code: 0
  result:
    id: 0
    principal: administrator@IPA.DEV.ENCORE.TECH
    result: null
    version: 4.5.0
  stderr: ''
  stdout: ''
```

The session string is passed into "cookies" while posting the request, thus, allowing for
Single Sign-On(SSO) rather than having to pass credentials for every action.

### <a name="Authentication"></a> Authentication

When logging in to a system and invoking commands you will need to authenticate
to login to the host, and maybe need to pass in a different set of credentials
to the cmdlet. When logging in to the remote system there are two ways to pass
in authentication credentials to the action.

#### Options:
- user/password parameters passed directly to the action
- connection parameter passed to the action
- session cookie string from login action

#### username/password parameters
In this case the user/password are specified where the action is invoked,
thus allowing you to pass in credentials on the commandline for easy testing.

``` shell
st2 run freeipa.host_add args='hostname' server='ipa.domain.tld' user='user@domain.com' password='Password1'
```

#### connection parameter
In this case the name of the connection to used is passed in where the action
is invoked, and the actual credentials themselves are stored in the pack's
configuration file `/opt/stackstorm/configs/freeipa.yaml`.

Let's say we had a configuration file with the contents:

``` yaml
---
connections:
  abc:
    user: "userexample"
    password: "passwordexample"
    server: "serverexample"
  test:
    user: ipaadminuser
    password: super secret
    server: same thing as hostname
```

We could invoke the login action using the `abc` credentials to login to `hostname` like so:

``` shell
st2 run freeipa.login connection=abc
..
id: 598dcaaaa2fb38cf298a297a
status: succeeded
parameters:
  connection: abc
result:
  exit_code: 0
  result: MagBearerToken=12345
  stderr: 'st2.actions.python.login: INFO     Successfully logged in as admin

    '
  stdout: ''
```

Similarly if we wanted to invoke the same action using the `test` credentials:

``` shell
st2 run freeipa.login connection=test
..
id: 598dcaaaa2fb38cf298a297a
status: succeeded
parameters:
  connection: abc
result:
  exit_code: 0
  result: MagBearerToken=12345
  stderr: 'st2.actions.python.login: INFO     Successfully logged in as admin

    '
  stdout: ''
```
The result session string is `MagBearerToken='12345'` which is then passes into any action for a single sign on.

``` shell
st2 run freeipa.host_add session='MagBearerToken=12345' args=ipahostname.domain.tld params=['all':True,'force':True]'
...
id: 598dcac0a2fb38cf298a2983
status: succeeded
parameters:
  args:
  - ipahostname.domain.tld
  params: {}
  server: ipahostname.domain.tld
  session: MagBearerToken=12345
result:
  exit_code: 0
  result:
    id: 0
    principal: administrator@IPA.DEV.ENCORE.TECH
    result: null
    version: 4.5.0
  stderr: ''
  stdout: ''
```

### session parameter
In this case the session cookie that is returned by the freeipa.login action, invoked by either 
[Basic Usage](#BasicUsage) or [Config Usage]($UsageConfig), is passed in where the action is invoked.

```shell
st2 run freeipa.login connection=abc
....
id: 598c977da2fb38cf298a28f9
status: succeeded
parameters:
  connection: abc
result:
  exit_code: 0
  result: MagBearerToken=abcdef
  stderr: 'st2.actions.python.login: INFO     Successfully logged in as administrator

    '
  stdout: ''
```

The result session string is `MagBearerToken='abcdef'` which is then passes into any action for a single sign on.

``` shell
st2 run freeipa.host_add session='MagBearerToken=abcdef' args=ipahostname.domain.tld params=['all':True,'force':True]'
...
id: 598dcac0a2fb38cf298a2983
status: succeeded
parameters:
  args:
  - ipahostname.domain.tld
  params: {}
  server: ipahostname.domain.tld
  session: MagBearerToken=abcdef
result:
  exit_code: 0
  result:
    id: 0
    principal: administrator@IPA.DEV.ENCORE.TECH
    result: null
    version: 4.5.0
  stderr: ''
  stdout: ''
```
