#!/usr/bin/env python

IPA_COMMAND_ARGS_OPTIONS = {
    "login": {
        "args": [
        ],
        "options": [
        ]
    },
    "aci_add": {
        "args": [
            "aciname",
        ],
        "options": [
            "aciprefix",
            "all",
            "attrs",
            "filter",
            "group",
            "memberof",
            "permission",
            "permissions",
            "raw",
            "selfaci",
            "subtree",
            "targetgroup",
            "test",
            "type",
            "version",
        ]
    },
    "aci_del": {
        "args": [
            "aciname",
        ],
        "options": [
            "aciprefix",
            "version",
        ]
    },
    "aci_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "aciname",
            "aciprefix",
            "all",
            "attrs",
            "filter",
            "group",
            "memberof",
            "permission",
            "permissions",
            "pkey_only",
            "raw",
            "selfaci",
            "subtree",
            "targetgroup",
            "type",
            "version",
        ]
    },
    "aci_mod": {
        "args": [
            "aciname",
        ],
        "options": [
            "aciprefix",
            "all",
            "attrs",
            "filter",
            "group",
            "memberof",
            "permission",
            "permissions",
            "raw",
            "selfaci",
            "subtree",
            "targetgroup",
            "type",
            "version",
        ]
    },
    "aci_rename": {
        "args": [
            "aciname",
        ],
        "options": [
            "aciprefix",
            "all",
            "attrs",
            "filter",
            "group",
            "memberof",
            "newname",
            "permission",
            "permissions",
            "raw",
            "selfaci",
            "subtree",
            "targetgroup",
            "type",
            "version",
        ]
    },
    "aci_show": {
        "args": [
            "aciname",
        ],
        "options": [
            "aciprefix",
            "all",
            "location",
            "raw",
            "version",
        ]
    },
    "adtrust_is_enabled": {
        "args": [
        ],
        "options": [
            "version",
        ]
    },
    "automember_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "raw",
            "setattr",
            "type",
            "version",
        ]
    },
    "automember_add_condition": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "automemberexclusiveregex",
            "automemberinclusiveregex",
            "description",
            "key",
            "raw",
            "type",
            "version",
        ]
    },
    "automember_default_group_remove": {
        "args": [
        ],
        "options": [
            "all",
            "description",
            "raw",
            "type",
            "version",
        ]
    },
    "automember_default_group_set": {
        "args": [
        ],
        "options": [
            "all",
            "automemberdefaultgroup",
            "description",
            "raw",
            "type",
            "version",
        ]
    },
    "automember_default_group_show": {
        "args": [
        ],
        "options": [
            "all",
            "raw",
            "type",
            "version",
        ]
    },
    "automember_del": {
        "args": [
            "cn",
        ],
        "options": [
            "type",
            "version",
        ]
    },
    "automember_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "description",
            "pkey_only",
            "raw",
            "type",
            "version",
        ]
    },
    "automember_find_orphans": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "description",
            "pkey_only",
            "raw",
            "remove",
            "type",
            "version",
        ]
    },
    "automember_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "raw",
            "rights",
            "setattr",
            "type",
            "version",
        ]
    },
    "automember_rebuild": {
        "args": [
        ],
        "options": [
            "all",
            "hosts",
            "no_wait",
            "raw",
            "type",
            "users",
            "version",
        ]
    },
    "automember_remove_condition": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "automemberexclusiveregex",
            "automemberinclusiveregex",
            "description",
            "key",
            "raw",
            "type",
            "version",
        ]
    },
    "automember_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "raw",
            "type",
            "version",
        ]
    },
    "automountkey_add": {
        "args": [
            "automountlocationcn",
            "automountmapautomountmapname",
        ],
        "options": [
            "addattr",
            "all",
            "automountinformation",
            "automountkey",
            "raw",
            "setattr",
            "version",
        ]
    },
    "automountkey_del": {
        "args": [
            "automountlocationcn",
            "automountmapautomountmapname",
        ],
        "options": [
            "automountinformation",
            "automountkey",
            "continue",
            "version",
        ]
    },
    "automountkey_find": {
        "args": [
            "automountlocationcn",
            "automountmapautomountmapname",
            "criteria",
        ],
        "options": [
            "all",
            "automountinformation",
            "automountkey",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "automountkey_mod": {
        "args": [
            "automountlocationcn",
            "automountmapautomountmapname",
        ],
        "options": [
            "addattr",
            "all",
            "automountinformation",
            "automountkey",
            "delattr",
            "newautomountinformation",
            "raw",
            "rename",
            "rights",
            "setattr",
            "version",
        ]
    },
    "automountkey_show": {
        "args": [
            "automountlocationcn",
            "automountmapautomountmapname",
        ],
        "options": [
            "all",
            "automountinformation",
            "automountkey",
            "raw",
            "rights",
            "version",
        ]
    },
    "automountlocation_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "raw",
            "setattr",
            "version",
        ]
    },
    "automountlocation_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "automountlocation_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "automountlocation_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "automountlocation_tofiles": {
        "args": [
            "cn",
        ],
        "options": [
            "version",
        ]
    },
    "automountmap_add": {
        "args": [
            "automountlocationcn",
            "automountmapname",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "raw",
            "setattr",
            "version",
        ]
    },
    "automountmap_add_indirect": {
        "args": [
            "automountlocationcn",
            "automountmapname",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "key",
            "parentmap",
            "raw",
            "setattr",
            "version",
        ]
    },
    "automountmap_del": {
        "args": [
            "automountlocationcn",
            "automountmapname",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "automountmap_find": {
        "args": [
            "automountlocationcn",
            "criteria",
        ],
        "options": [
            "all",
            "automountmapname",
            "description",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "automountmap_mod": {
        "args": [
            "automountlocationcn",
            "automountmapname",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "automountmap_show": {
        "args": [
            "automountlocationcn",
            "automountmapname",
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "batch": {
        "args": [
            "methods",
        ],
        "options": [
            "version",
        ]
    },
    "ca_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "chain",
            "description",
            "ipacasubjectdn",
            "raw",
            "setattr",
            "version",
        ]
    },
    "ca_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "ca_disable": {
        "args": [
            "cn",
        ],
        "options": [
            "version",
        ]
    },
    "ca_enable": {
        "args": [
            "cn",
        ],
        "options": [
            "version",
        ]
    },
    "ca_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "description",
            "ipacaid",
            "ipacaissuerdn",
            "ipacasubjectdn",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "ca_is_enabled": {
        "args": [
        ],
        "options": [
            "version",
        ]
    },
    "ca_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "raw",
            "rename",
            "rights",
            "setattr",
            "version",
        ]
    },
    "ca_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "chain",
            "raw",
            "rights",
            "version",
        ]
    },
    "caacl_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "hostcategory",
            "ipacacategory",
            "ipacertprofilecategory",
            "ipaenabledflag",
            "no_members",
            "raw",
            "servicecategory",
            "setattr",
            "usercategory",
            "version",
        ]
    },
    "caacl_add_ca": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "ca",
            "no_members",
            "raw",
            "version",
        ]
    },
    "caacl_add_host": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "version",
        ]
    },
    "caacl_add_profile": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "certprofile",
            "no_members",
            "raw",
            "version",
        ]
    },
    "caacl_add_service": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "service",
            "version",
        ]
    },
    "caacl_add_user": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "caacl_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "caacl_disable": {
        "args": [
            "cn",
        ],
        "options": [
            "version",
        ]
    },
    "caacl_enable": {
        "args": [
            "cn",
        ],
        "options": [
            "version",
        ]
    },
    "caacl_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "description",
            "hostcategory",
            "ipacacategory",
            "ipacertprofilecategory",
            "ipaenabledflag",
            "no_members",
            "pkey_only",
            "raw",
            "servicecategory",
            "sizelimit",
            "timelimit",
            "usercategory",
            "version",
        ]
    },
    "caacl_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "hostcategory",
            "ipacacategory",
            "ipacertprofilecategory",
            "ipaenabledflag",
            "no_members",
            "raw",
            "rights",
            "servicecategory",
            "setattr",
            "usercategory",
            "version",
        ]
    },
    "caacl_remove_ca": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "ca",
            "no_members",
            "raw",
            "version",
        ]
    },
    "caacl_remove_host": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "version",
        ]
    },
    "caacl_remove_profile": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "certprofile",
            "no_members",
            "raw",
            "version",
        ]
    },
    "caacl_remove_service": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "service",
            "version",
        ]
    },
    "caacl_remove_user": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "caacl_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "version",
        ]
    },
    "cert_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cacn",
            "certificate",
            "exactly",
            "host",
            "issuedon_from",
            "issuedon_to",
            "issuer",
            "max_serial_number",
            "min_serial_number",
            "no_host",
            "no_members",
            "no_service",
            "no_user",
            "pkey_only",
            "raw",
            "revocation_reason",
            "revokedon_from",
            "revokedon_to",
            "service",
            "sizelimit",
            "subject",
            "timelimit",
            "user",
            "validnotafter_from",
            "validnotafter_to",
            "validnotbefore_from",
            "validnotbefore_to",
            "version",
        ]
    },
    "cert_remove_hold": {
        "args": [
            "serial_number",
        ],
        "options": [
            "cacn",
            "version",
        ]
    },
    "cert_request": {
        "args": [
            "csr",
        ],
        "options": [
            "add",
            "all",
            "cacn",
            "chain",
            "principal",
            "profile_id",
            "raw",
            "request_type",
            "version",
        ]
    },
    "cert_revoke": {
        "args": [
            "serial_number",
        ],
        "options": [
            "cacn",
            "revocation_reason",
            "version",
        ]
    },
    "cert_show": {
        "args": [
            "serial_number",
        ],
        "options": [
            "all",
            "cacn",
            "chain",
            "no_members",
            "out",
            "raw",
            "version",
        ]
    },
    "cert_status": {
        "args": [
            "request_id",
        ],
        "options": [
            "all",
            "cacn",
            "raw",
            "version",
        ]
    },
    "certmap_match": {
        "args": [
            "certificate",
        ],
        "options": [
            "all",
            "raw",
            "version",
        ]
    },
    "certmapconfig_mod": {
        "args": [
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "ipacertmappromptusername",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "certmapconfig_show": {
        "args": [
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "certmaprule_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "associateddomain",
            "description",
            "ipacertmapmaprule",
            "ipacertmapmatchrule",
            "ipacertmappriority",
            "ipaenabledflag",
            "raw",
            "setattr",
            "version",
        ]
    },
    "certmaprule_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "certmaprule_disable": {
        "args": [
            "cn",
        ],
        "options": [
            "version",
        ]
    },
    "certmaprule_enable": {
        "args": [
            "cn",
        ],
        "options": [
            "version",
        ]
    },
    "certmaprule_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "associateddomain",
            "cn",
            "description",
            "ipacertmapmaprule",
            "ipacertmapmatchrule",
            "ipacertmappriority",
            "ipaenabledflag",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "certmaprule_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "associateddomain",
            "delattr",
            "description",
            "ipacertmapmaprule",
            "ipacertmapmatchrule",
            "ipacertmappriority",
            "ipaenabledflag",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "certmaprule_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "certprofile_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "certprofile_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "description",
            "ipacertprofilestoreissued",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "certprofile_import": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "description",
            "file",
            "ipacertprofilestoreissued",
            "raw",
            "version",
        ]
    },
    "certprofile_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "file",
            "ipacertprofilestoreissued",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "certprofile_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "out",
            "raw",
            "rights",
            "version",
        ]
    },
    "class_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "pkey_only",
            "raw",
            "version",
        ]
    },
    "class_show": {
        "args": [
            "full_name",
        ],
        "options": [
            "all",
            "raw",
            "version",
        ]
    },
    "command_defaults": {
        "args": [
            "full_name",
        ],
        "options": [
            "kw",
            "params",
            "version",
        ]
    },
    "command_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "pkey_only",
            "raw",
            "version",
        ]
    },
    "command_show": {
        "args": [
            "full_name",
        ],
        "options": [
            "all",
            "raw",
            "version",
        ]
    },
    "compat_is_enabled": {
        "args": [
        ],
        "options": [
            "version",
        ]
    },
    "config_mod": {
        "args": [
        ],
        "options": [
            "addattr",
            "all",
            "ca_renewal_master_server",
            "delattr",
            "ipaconfigstring",
            "ipadefaultemaildomain",
            "ipadefaultloginshell",
            "ipadefaultprimarygroup",
            "ipadomainresolutionorder",
            "ipagroupobjectclasses",
            "ipagroupsearchfields",
            "ipahomesrootdir",
            "ipakrbauthzdata",
            "ipamaxusernamelength",
            "ipamigrationenabled",
            "ipapwdexpadvnotify",
            "ipasearchrecordslimit",
            "ipasearchtimelimit",
            "ipaselinuxusermapdefault",
            "ipaselinuxusermaporder",
            "ipauserauthtype",
            "ipauserobjectclasses",
            "ipausersearchfields",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "config_show": {
        "args": [
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "cosentry_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "cospriority",
            "krbpwdpolicyreference",
            "raw",
            "setattr",
            "version",
        ]
    },
    "cosentry_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "cosentry_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "cospriority",
            "krbpwdpolicyreference",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "cosentry_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "cospriority",
            "delattr",
            "krbpwdpolicyreference",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "cosentry_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "delegation_add": {
        "args": [
            "aciname",
        ],
        "options": [
            "all",
            "attrs",
            "group",
            "memberof",
            "permissions",
            "raw",
            "version",
        ]
    },
    "delegation_del": {
        "args": [
            "aciname",
        ],
        "options": [
            "version",
        ]
    },
    "delegation_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "aciname",
            "all",
            "attrs",
            "group",
            "memberof",
            "permissions",
            "pkey_only",
            "raw",
            "version",
        ]
    },
    "delegation_mod": {
        "args": [
            "aciname",
        ],
        "options": [
            "all",
            "attrs",
            "group",
            "memberof",
            "permissions",
            "raw",
            "version",
        ]
    },
    "delegation_show": {
        "args": [
            "aciname",
        ],
        "options": [
            "all",
            "raw",
            "version",
        ]
    },
    "dns_is_enabled": {
        "args": [
        ],
        "options": [
            "version",
        ]
    },
    "dns_resolve": {
        "args": [
            "hostname",
        ],
        "options": [
            "version",
        ]
    },
    "dns_update_system_records": {
        "args": [
        ],
        "options": [
            "all",
            "dry_run",
            "raw",
            "version",
        ]
    },
    "dnsconfig_mod": {
        "args": [
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "idnsallowsyncptr",
            "idnsforwarders",
            "idnsforwardpolicy",
            "idnszonerefresh",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "dnsconfig_show": {
        "args": [
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "dnsforwardzone_add": {
        "args": [
            "idnsname",
        ],
        "options": [
            "addattr",
            "all",
            "idnsforwarders",
            "idnsforwardpolicy",
            "name_from_ip",
            "raw",
            "setattr",
            "skip_overlap_check",
            "version",
        ]
    },
    "dnsforwardzone_add_permission": {
        "args": [
            "idnsname",
        ],
        "options": [
            "version",
        ]
    },
    "dnsforwardzone_del": {
        "args": [
            "idnsname",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "dnsforwardzone_disable": {
        "args": [
            "idnsname",
        ],
        "options": [
            "version",
        ]
    },
    "dnsforwardzone_enable": {
        "args": [
            "idnsname",
        ],
        "options": [
            "version",
        ]
    },
    "dnsforwardzone_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "idnsforwarders",
            "idnsforwardpolicy",
            "idnsname",
            "idnszoneactive",
            "name_from_ip",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "dnsforwardzone_mod": {
        "args": [
            "idnsname",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "idnsforwarders",
            "idnsforwardpolicy",
            "name_from_ip",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "dnsforwardzone_remove_permission": {
        "args": [
            "idnsname",
        ],
        "options": [
            "version",
        ]
    },
    "dnsforwardzone_show": {
        "args": [
            "idnsname",
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "dnsrecord_add": {
        "args": [
            "dnszoneidnsname",
            "idnsname",
        ],
        "options": [
            "a6_part_data",
            "a6record",
            "a_extra_create_reverse",
            "a_part_ip_address",
            "aaaa_extra_create_reverse",
            "aaaa_part_ip_address",
            "aaaarecord",
            "addattr",
            "afsdb_part_hostname",
            "afsdb_part_subtype",
            "afsdbrecord",
            "all",
            "aplrecord",
            "arecord",
            "cert_part_algorithm",
            "cert_part_certificate_or_crl",
            "cert_part_key_tag",
            "cert_part_type",
            "certrecord",
            "cname_part_hostname",
            "cnamerecord",
            "dhcidrecord",
            "dlv_part_algorithm",
            "dlv_part_digest",
            "dlv_part_digest_type",
            "dlv_part_key_tag",
            "dlvrecord",
            "dname_part_target",
            "dnamerecord",
            "dnsclass",
            "dnsttl",
            "ds_part_algorithm",
            "ds_part_digest",
            "ds_part_digest_type",
            "ds_part_key_tag",
            "dsrecord",
            "force",
            "hiprecord",
            "ipseckeyrecord",
            "keyrecord",
            "kx_part_exchanger",
            "kx_part_preference",
            "kxrecord",
            "loc_part_altitude",
            "loc_part_h_precision",
            "loc_part_lat_deg",
            "loc_part_lat_dir",
            "loc_part_lat_min",
            "loc_part_lat_sec",
            "loc_part_lon_deg",
            "loc_part_lon_dir",
            "loc_part_lon_min",
            "loc_part_lon_sec",
            "loc_part_size",
            "loc_part_v_precision",
            "locrecord",
            "mx_part_exchanger",
            "mx_part_preference",
            "mxrecord",
            "naptr_part_flags",
            "naptr_part_order",
            "naptr_part_preference",
            "naptr_part_regexp",
            "naptr_part_replacement",
            "naptr_part_service",
            "naptrrecord",
            "ns_part_hostname",
            "nsecrecord",
            "nsrecord",
            "ptr_part_hostname",
            "ptrrecord",
            "raw",
            "rprecord",
            "rrsigrecord",
            "setattr",
            "sigrecord",
            "spfrecord",
            "srv_part_port",
            "srv_part_priority",
            "srv_part_target",
            "srv_part_weight",
            "srvrecord",
            "sshfp_part_algorithm",
            "sshfp_part_fingerprint",
            "sshfp_part_fp_type",
            "sshfprecord",
            "structured",
            "tlsa_part_cert_association_data",
            "tlsa_part_cert_usage",
            "tlsa_part_matching_type",
            "tlsa_part_selector",
            "tlsarecord",
            "txt_part_data",
            "txtrecord",
            "uri_part_priority",
            "uri_part_target",
            "uri_part_weight",
            "urirecord",
            "version",
        ]
    },
    "dnsrecord_del": {
        "args": [
            "dnszoneidnsname",
            "idnsname",
        ],
        "options": [
            "a6record",
            "aaaarecord",
            "afsdbrecord",
            "aplrecord",
            "arecord",
            "certrecord",
            "cnamerecord",
            "del_all",
            "dhcidrecord",
            "dlvrecord",
            "dnamerecord",
            "dnsclass",
            "dnsttl",
            "dsrecord",
            "hiprecord",
            "ipseckeyrecord",
            "keyrecord",
            "kxrecord",
            "locrecord",
            "mxrecord",
            "naptrrecord",
            "nsecrecord",
            "nsrecord",
            "ptrrecord",
            "raw",
            "rprecord",
            "rrsigrecord",
            "sigrecord",
            "spfrecord",
            "srvrecord",
            "sshfprecord",
            "structured",
            "tlsarecord",
            "txtrecord",
            "urirecord",
            "version",
        ]
    },
    "dnsrecord_delentry": {
        "args": [
            "dnszoneidnsname",
            "idnsname",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "dnsrecord_find": {
        "args": [
            "dnszoneidnsname",
            "criteria",
        ],
        "options": [
            "a6record",
            "aaaarecord",
            "afsdbrecord",
            "all",
            "aplrecord",
            "arecord",
            "certrecord",
            "cnamerecord",
            "dhcidrecord",
            "dlvrecord",
            "dnamerecord",
            "dnsclass",
            "dnsttl",
            "dsrecord",
            "hiprecord",
            "idnsname",
            "ipseckeyrecord",
            "keyrecord",
            "kxrecord",
            "locrecord",
            "mxrecord",
            "naptrrecord",
            "nsecrecord",
            "nsrecord",
            "pkey_only",
            "ptrrecord",
            "raw",
            "rprecord",
            "rrsigrecord",
            "sigrecord",
            "sizelimit",
            "spfrecord",
            "srvrecord",
            "sshfprecord",
            "structured",
            "timelimit",
            "tlsarecord",
            "txtrecord",
            "urirecord",
            "version",
        ]
    },
    "dnsrecord_mod": {
        "args": [
            "dnszoneidnsname",
            "idnsname",
        ],
        "options": [
            "a6_part_data",
            "a6record",
            "a_part_ip_address",
            "aaaa_part_ip_address",
            "aaaarecord",
            "addattr",
            "afsdb_part_hostname",
            "afsdb_part_subtype",
            "afsdbrecord",
            "all",
            "aplrecord",
            "arecord",
            "cert_part_algorithm",
            "cert_part_certificate_or_crl",
            "cert_part_key_tag",
            "cert_part_type",
            "certrecord",
            "cname_part_hostname",
            "cnamerecord",
            "delattr",
            "dhcidrecord",
            "dlv_part_algorithm",
            "dlv_part_digest",
            "dlv_part_digest_type",
            "dlv_part_key_tag",
            "dlvrecord",
            "dname_part_target",
            "dnamerecord",
            "dnsclass",
            "dnsttl",
            "ds_part_algorithm",
            "ds_part_digest",
            "ds_part_digest_type",
            "ds_part_key_tag",
            "dsrecord",
            "hiprecord",
            "ipseckeyrecord",
            "keyrecord",
            "kx_part_exchanger",
            "kx_part_preference",
            "kxrecord",
            "loc_part_altitude",
            "loc_part_h_precision",
            "loc_part_lat_deg",
            "loc_part_lat_dir",
            "loc_part_lat_min",
            "loc_part_lat_sec",
            "loc_part_lon_deg",
            "loc_part_lon_dir",
            "loc_part_lon_min",
            "loc_part_lon_sec",
            "loc_part_size",
            "loc_part_v_precision",
            "locrecord",
            "mx_part_exchanger",
            "mx_part_preference",
            "mxrecord",
            "naptr_part_flags",
            "naptr_part_order",
            "naptr_part_preference",
            "naptr_part_regexp",
            "naptr_part_replacement",
            "naptr_part_service",
            "naptrrecord",
            "ns_part_hostname",
            "nsecrecord",
            "nsrecord",
            "ptr_part_hostname",
            "ptrrecord",
            "raw",
            "rename",
            "rights",
            "rprecord",
            "rrsigrecord",
            "setattr",
            "sigrecord",
            "spfrecord",
            "srv_part_port",
            "srv_part_priority",
            "srv_part_target",
            "srv_part_weight",
            "srvrecord",
            "sshfp_part_algorithm",
            "sshfp_part_fingerprint",
            "sshfp_part_fp_type",
            "sshfprecord",
            "structured",
            "tlsa_part_cert_association_data",
            "tlsa_part_cert_usage",
            "tlsa_part_matching_type",
            "tlsa_part_selector",
            "tlsarecord",
            "txt_part_data",
            "txtrecord",
            "uri_part_priority",
            "uri_part_target",
            "uri_part_weight",
            "urirecord",
            "version",
        ]
    },
    "dnsrecord_show": {
        "args": [
            "dnszoneidnsname",
            "idnsname",
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "structured",
            "version",
        ]
    },
    "dnsrecord_split_parts": {
        "args": [
            "name",
            "value",
        ],
        "options": [
            "version",
        ]
    },
    "dnsserver_add": {
        "args": [
            "idnsserverid",
        ],
        "options": [
            "addattr",
            "all",
            "idnsforwarders",
            "idnsforwardpolicy",
            "idnssoamname",
            "raw",
            "setattr",
            "version",
        ]
    },
    "dnsserver_del": {
        "args": [
            "idnsserverid",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "dnsserver_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "idnsforwarders",
            "idnsforwardpolicy",
            "idnsserverid",
            "idnssoamname",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "dnsserver_mod": {
        "args": [
            "idnsserverid",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "idnsforwarders",
            "idnsforwardpolicy",
            "idnssoamname",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "dnsserver_show": {
        "args": [
            "idnsserverid",
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "dnszone_add": {
        "args": [
            "idnsname",
        ],
        "options": [
            "addattr",
            "all",
            "dnsclass",
            "dnsdefaultttl",
            "dnsttl",
            "force",
            "idnsallowdynupdate",
            "idnsallowquery",
            "idnsallowsyncptr",
            "idnsallowtransfer",
            "idnsforwarders",
            "idnsforwardpolicy",
            "idnssecinlinesigning",
            "idnssoaexpire",
            "idnssoaminimum",
            "idnssoamname",
            "idnssoarefresh",
            "idnssoaretry",
            "idnssoarname",
            "idnssoaserial",
            "idnsupdatepolicy",
            "ip_address",
            "name_from_ip",
            "nsec3paramrecord",
            "raw",
            "setattr",
            "skip_nameserver_check",
            "skip_overlap_check",
            "version",
        ]
    },
    "dnszone_add_permission": {
        "args": [
            "idnsname",
        ],
        "options": [
            "version",
        ]
    },
    "dnszone_del": {
        "args": [
            "idnsname",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "dnszone_disable": {
        "args": [
            "idnsname",
        ],
        "options": [
            "version",
        ]
    },
    "dnszone_enable": {
        "args": [
            "idnsname",
        ],
        "options": [
            "version",
        ]
    },
    "dnszone_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "dnsclass",
            "dnsdefaultttl",
            "dnsttl",
            "forward_only",
            "idnsallowdynupdate",
            "idnsallowquery",
            "idnsallowsyncptr",
            "idnsallowtransfer",
            "idnsforwarders",
            "idnsforwardpolicy",
            "idnsname",
            "idnssecinlinesigning",
            "idnssoaexpire",
            "idnssoaminimum",
            "idnssoamname",
            "idnssoarefresh",
            "idnssoaretry",
            "idnssoarname",
            "idnssoaserial",
            "idnsupdatepolicy",
            "idnszoneactive",
            "name_from_ip",
            "nsec3paramrecord",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "dnszone_mod": {
        "args": [
            "idnsname",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "dnsclass",
            "dnsdefaultttl",
            "dnsttl",
            "force",
            "idnsallowdynupdate",
            "idnsallowquery",
            "idnsallowsyncptr",
            "idnsallowtransfer",
            "idnsforwarders",
            "idnsforwardpolicy",
            "idnssecinlinesigning",
            "idnssoaexpire",
            "idnssoaminimum",
            "idnssoamname",
            "idnssoarefresh",
            "idnssoaretry",
            "idnssoarname",
            "idnssoaserial",
            "idnsupdatepolicy",
            "name_from_ip",
            "nsec3paramrecord",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "dnszone_remove_permission": {
        "args": [
            "idnsname",
        ],
        "options": [
            "version",
        ]
    },
    "dnszone_show": {
        "args": [
            "idnsname",
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "domainlevel_get": {
        "args": [
        ],
        "options": [
            "version",
        ]
    },
    "domainlevel_set": {
        "args": [
            "ipadomainlevel",
        ],
        "options": [
            "version",
        ]
    },
    "env": {
        "args": [
            "variables",
        ],
        "options": [
            "all",
            "server",
            "version",
        ]
    },
    "group_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "external",
            "gidnumber",
            "no_members",
            "nonposix",
            "raw",
            "setattr",
            "version",
        ]
    },
    "group_add_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "ipaexternalmember",
            "no_members",
            "raw",
            "service",
            "user",
            "version",
        ]
    },
    "group_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "group_detach": {
        "args": [
            "cn",
        ],
        "options": [
            "version",
        ]
    },
    "group_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "description",
            "external",
            "gidnumber",
            "group",
            "in_group",
            "in_hbacrule",
            "in_netgroup",
            "in_role",
            "in_sudorule",
            "no_group",
            "no_members",
            "no_service",
            "no_user",
            "nonposix",
            "not_in_group",
            "not_in_hbacrule",
            "not_in_netgroup",
            "not_in_role",
            "not_in_sudorule",
            "pkey_only",
            "posix",
            "private",
            "raw",
            "service",
            "sizelimit",
            "timelimit",
            "user",
            "version",
        ]
    },
    "group_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "external",
            "gidnumber",
            "no_members",
            "posix",
            "raw",
            "rename",
            "rights",
            "setattr",
            "version",
        ]
    },
    "group_remove_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "ipaexternalmember",
            "no_members",
            "raw",
            "service",
            "user",
            "version",
        ]
    },
    "group_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "version",
        ]
    },
    "hbacrule_add": {
        "args": [
            "cn",
        ],
        "options": [
            "accessruletype",
            "addattr",
            "all",
            "description",
            "externalhost",
            "hostcategory",
            "ipaenabledflag",
            "no_members",
            "raw",
            "servicecategory",
            "setattr",
            "sourcehostcategory",
            "usercategory",
            "version",
        ]
    },
    "hbacrule_add_host": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "version",
        ]
    },
    "hbacrule_add_service": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "hbacsvc",
            "hbacsvcgroup",
            "no_members",
            "raw",
            "version",
        ]
    },
    "hbacrule_add_sourcehost": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "version",
        ]
    },
    "hbacrule_add_user": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "hbacrule_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "hbacrule_disable": {
        "args": [
            "cn",
        ],
        "options": [
            "version",
        ]
    },
    "hbacrule_enable": {
        "args": [
            "cn",
        ],
        "options": [
            "version",
        ]
    },
    "hbacrule_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "accessruletype",
            "all",
            "cn",
            "description",
            "externalhost",
            "hostcategory",
            "ipaenabledflag",
            "no_members",
            "pkey_only",
            "raw",
            "servicecategory",
            "sizelimit",
            "sourcehostcategory",
            "timelimit",
            "usercategory",
            "version",
        ]
    },
    "hbacrule_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "accessruletype",
            "addattr",
            "all",
            "delattr",
            "description",
            "externalhost",
            "hostcategory",
            "ipaenabledflag",
            "no_members",
            "raw",
            "rename",
            "rights",
            "servicecategory",
            "setattr",
            "sourcehostcategory",
            "usercategory",
            "version",
        ]
    },
    "hbacrule_remove_host": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "version",
        ]
    },
    "hbacrule_remove_service": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "hbacsvc",
            "hbacsvcgroup",
            "no_members",
            "raw",
            "version",
        ]
    },
    "hbacrule_remove_sourcehost": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "version",
        ]
    },
    "hbacrule_remove_user": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "hbacrule_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "version",
        ]
    },
    "hbacsvc_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "no_members",
            "raw",
            "setattr",
            "version",
        ]
    },
    "hbacsvc_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "hbacsvc_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "description",
            "no_members",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "hbacsvc_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "no_members",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "hbacsvc_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "version",
        ]
    },
    "hbacsvcgroup_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "no_members",
            "raw",
            "setattr",
            "version",
        ]
    },
    "hbacsvcgroup_add_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "hbacsvc",
            "no_members",
            "raw",
            "version",
        ]
    },
    "hbacsvcgroup_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "hbacsvcgroup_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "description",
            "no_members",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "hbacsvcgroup_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "no_members",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "hbacsvcgroup_remove_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "hbacsvc",
            "no_members",
            "raw",
            "version",
        ]
    },
    "hbacsvcgroup_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "version",
        ]
    },
    "hbactest": {
        "args": [
        ],
        "options": [
            "disabled",
            "enabled",
            "nodetail",
            "rules",
            "service",
            "sizelimit",
            "sourcehost",
            "targethost",
            "user",
            "version",
        ]
    },
    "host_add": {
        "args": [
            "fqdn",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "force",
            "ip_address",
            "ipaassignedidview",
            "ipakrbokasdelegate",
            "ipakrboktoauthasdelegate",
            "ipakrbrequirespreauth",
            "ipasshpubkey",
            "krbprincipalauthind",
            "l",
            "macaddress",
            "no_members",
            "no_reverse",
            "nshardwareplatform",
            "nshostlocation",
            "nsosversion",
            "random",
            "raw",
            "setattr",
            "usercertificate",
            "userclass",
            "userpassword",
            "version",
        ]
    },
    "host_add_cert": {
        "args": [
            "fqdn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "usercertificate",
            "version",
        ]
    },
    "host_add_managedby": {
        "args": [
            "fqdn",
        ],
        "options": [
            "all",
            "host",
            "no_members",
            "raw",
            "version",
        ]
    },
    "host_add_principal": {
        "args": [
            "fqdn",
            "krbprincipalname",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "version",
        ]
    },
    "host_allow_create_keytab": {
        "args": [
            "fqdn",
        ],
        "options": [
            "all",
            "group",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "host_allow_retrieve_keytab": {
        "args": [
            "fqdn",
        ],
        "options": [
            "all",
            "group",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "host_del": {
        "args": [
            "fqdn",
        ],
        "options": [
            "continue",
            "updatedns",
            "version",
        ]
    },
    "host_disable": {
        "args": [
            "fqdn",
        ],
        "options": [
            "version",
        ]
    },
    "host_disallow_create_keytab": {
        "args": [
            "fqdn",
        ],
        "options": [
            "all",
            "group",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "host_disallow_retrieve_keytab": {
        "args": [
            "fqdn",
        ],
        "options": [
            "all",
            "group",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "host_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "description",
            "enroll_by_user",
            "fqdn",
            "in_hbacrule",
            "in_hostgroup",
            "in_netgroup",
            "in_role",
            "in_sudorule",
            "ipaassignedidview",
            "krbprincipalauthind",
            "l",
            "macaddress",
            "man_by_host",
            "man_host",
            "no_members",
            "not_enroll_by_user",
            "not_in_hbacrule",
            "not_in_hostgroup",
            "not_in_netgroup",
            "not_in_role",
            "not_in_sudorule",
            "not_man_by_host",
            "not_man_host",
            "nshardwareplatform",
            "nshostlocation",
            "nsosversion",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "usercertificate",
            "userclass",
            "userpassword",
            "version",
        ]
    },
    "host_mod": {
        "args": [
            "fqdn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "ipaassignedidview",
            "ipakrbokasdelegate",
            "ipakrboktoauthasdelegate",
            "ipakrbrequirespreauth",
            "ipasshpubkey",
            "krbprincipalauthind",
            "krbprincipalname",
            "l",
            "macaddress",
            "no_members",
            "nshardwareplatform",
            "nshostlocation",
            "nsosversion",
            "random",
            "raw",
            "rights",
            "setattr",
            "updatedns",
            "usercertificate",
            "userclass",
            "userpassword",
            "version",
        ]
    },
    "host_remove_cert": {
        "args": [
            "fqdn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "usercertificate",
            "version",
        ]
    },
    "host_remove_managedby": {
        "args": [
            "fqdn",
        ],
        "options": [
            "all",
            "host",
            "no_members",
            "raw",
            "version",
        ]
    },
    "host_remove_principal": {
        "args": [
            "fqdn",
            "krbprincipalname",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "version",
        ]
    },
    "host_show": {
        "args": [
            "fqdn",
        ],
        "options": [
            "all",
            "no_members",
            "out",
            "raw",
            "rights",
            "version",
        ]
    },
    "hostgroup_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "no_members",
            "raw",
            "setattr",
            "version",
        ]
    },
    "hostgroup_add_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "version",
        ]
    },
    "hostgroup_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "hostgroup_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "description",
            "host",
            "hostgroup",
            "in_hbacrule",
            "in_hostgroup",
            "in_netgroup",
            "in_sudorule",
            "no_host",
            "no_hostgroup",
            "no_members",
            "not_in_hbacrule",
            "not_in_hostgroup",
            "not_in_netgroup",
            "not_in_sudorule",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "hostgroup_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "no_members",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "hostgroup_remove_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "version",
        ]
    },
    "hostgroup_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "version",
        ]
    },
    "i18n_messages": {
        "args": [
        ],
        "options": [
            "version",
        ]
    },
    "idoverridegroup_add": {
        "args": [
            "idviewcn",
            "ipaanchoruuid",
        ],
        "options": [
            "addattr",
            "all",
            "cn",
            "description",
            "fallback_to_ldap",
            "gidnumber",
            "raw",
            "setattr",
            "version",
        ]
    },
    "idoverridegroup_del": {
        "args": [
            "idviewcn",
            "ipaanchoruuid",
        ],
        "options": [
            "continue",
            "fallback_to_ldap",
            "version",
        ]
    },
    "idoverridegroup_find": {
        "args": [
            "idviewcn",
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "description",
            "fallback_to_ldap",
            "gidnumber",
            "ipaanchoruuid",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "idoverridegroup_mod": {
        "args": [
            "idviewcn",
            "ipaanchoruuid",
        ],
        "options": [
            "addattr",
            "all",
            "cn",
            "delattr",
            "description",
            "fallback_to_ldap",
            "gidnumber",
            "raw",
            "rename",
            "rights",
            "setattr",
            "version",
        ]
    },
    "idoverridegroup_show": {
        "args": [
            "idviewcn",
            "ipaanchoruuid",
        ],
        "options": [
            "all",
            "fallback_to_ldap",
            "raw",
            "rights",
            "version",
        ]
    },
    "idoverrideuser_add": {
        "args": [
            "idviewcn",
            "ipaanchoruuid",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "fallback_to_ldap",
            "gecos",
            "gidnumber",
            "homedirectory",
            "ipaoriginaluid",
            "ipasshpubkey",
            "loginshell",
            "raw",
            "setattr",
            "uid",
            "uidnumber",
            "usercertificate",
            "version",
        ]
    },
    "idoverrideuser_add_cert": {
        "args": [
            "idviewcn",
            "ipaanchoruuid",
        ],
        "options": [
            "all",
            "fallback_to_ldap",
            "raw",
            "usercertificate",
            "version",
        ]
    },
    "idoverrideuser_del": {
        "args": [
            "idviewcn",
            "ipaanchoruuid",
        ],
        "options": [
            "continue",
            "fallback_to_ldap",
            "version",
        ]
    },
    "idoverrideuser_find": {
        "args": [
            "idviewcn",
            "criteria",
        ],
        "options": [
            "all",
            "description",
            "fallback_to_ldap",
            "gecos",
            "gidnumber",
            "homedirectory",
            "ipaanchoruuid",
            "ipaoriginaluid",
            "loginshell",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "uid",
            "uidnumber",
            "version",
        ]
    },
    "idoverrideuser_mod": {
        "args": [
            "idviewcn",
            "ipaanchoruuid",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "fallback_to_ldap",
            "gecos",
            "gidnumber",
            "homedirectory",
            "ipaoriginaluid",
            "ipasshpubkey",
            "loginshell",
            "raw",
            "rename",
            "rights",
            "setattr",
            "uid",
            "uidnumber",
            "usercertificate",
            "version",
        ]
    },
    "idoverrideuser_remove_cert": {
        "args": [
            "idviewcn",
            "ipaanchoruuid",
        ],
        "options": [
            "all",
            "fallback_to_ldap",
            "raw",
            "usercertificate",
            "version",
        ]
    },
    "idoverrideuser_show": {
        "args": [
            "idviewcn",
            "ipaanchoruuid",
        ],
        "options": [
            "all",
            "fallback_to_ldap",
            "raw",
            "rights",
            "version",
        ]
    },
    "idrange_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "ipabaseid",
            "ipabaserid",
            "ipaidrangesize",
            "ipanttrusteddomainname",
            "ipanttrusteddomainsid",
            "iparangetype",
            "ipasecondarybaserid",
            "raw",
            "setattr",
            "version",
        ]
    },
    "idrange_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "idrange_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "ipabaseid",
            "ipabaserid",
            "ipaidrangesize",
            "ipanttrusteddomainsid",
            "iparangetype",
            "ipasecondarybaserid",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "idrange_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "ipabaseid",
            "ipabaserid",
            "ipaidrangesize",
            "ipanttrusteddomainname",
            "ipanttrusteddomainsid",
            "ipasecondarybaserid",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "idrange_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "idview_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "ipadomainresolutionorder",
            "raw",
            "setattr",
            "version",
        ]
    },
    "idview_apply": {
        "args": [
            "cn",
        ],
        "options": [
            "host",
            "hostgroup",
            "version",
        ]
    },
    "idview_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "idview_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "description",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "idview_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "ipadomainresolutionorder",
            "raw",
            "rename",
            "rights",
            "setattr",
            "version",
        ]
    },
    "idview_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "show_hosts",
            "version",
        ]
    },
    "idview_unapply": {
        "args": [
        ],
        "options": [
            "host",
            "hostgroup",
            "version",
        ]
    },
    "join": {
        "args": [
            "cn",
        ],
        "options": [
            "nshardwareplatform",
            "nsosversion",
            "realm",
            "version",
        ]
    },
    "json_metadata": {
        "args": [
            "objname",
            "methodname",
        ],
        "options": [
            "command",
            "method",
            "object",
            "version",
        ]
    },
    "kra_is_enabled": {
        "args": [
        ],
        "options": [
            "version",
        ]
    },
    "krbtpolicy_mod": {
        "args": [
            "uid",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "krbmaxrenewableage",
            "krbmaxticketlife",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "krbtpolicy_reset": {
        "args": [
            "uid",
        ],
        "options": [
            "all",
            "raw",
            "version",
        ]
    },
    "krbtpolicy_show": {
        "args": [
            "uid",
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "location_add": {
        "args": [
            "idnsname",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "raw",
            "setattr",
            "version",
        ]
    },
    "location_del": {
        "args": [
            "idnsname",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "location_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "description",
            "idnsname",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "location_mod": {
        "args": [
            "idnsname",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "location_show": {
        "args": [
            "idnsname",
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "migrate_ds": {
        "args": [
            "ldapuri",
            "bindpw",
        ],
        "options": [
            "basedn",
            "binddn",
            "cacertfile",
            "compat",
            "continue",
            "exclude_groups",
            "exclude_users",
            "groupcontainer",
            "groupignoreattribute",
            "groupignoreobjectclass",
            "groupobjectclass",
            "groupoverwritegid",
            "schema",
            "scope",
            "use_def_group",
            "usercontainer",
            "userignoreattribute",
            "userignoreobjectclass",
            "userobjectclass",
            "version",
        ]
    },
    "netgroup_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "externalhost",
            "hostcategory",
            "nisdomainname",
            "no_members",
            "raw",
            "setattr",
            "usercategory",
            "version",
        ]
    },
    "netgroup_add_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "host",
            "hostgroup",
            "netgroup",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "netgroup_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "netgroup_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "description",
            "externalhost",
            "group",
            "host",
            "hostcategory",
            "hostgroup",
            "in_netgroup",
            "ipauniqueid",
            "managed",
            "netgroup",
            "nisdomainname",
            "no_group",
            "no_host",
            "no_hostgroup",
            "no_members",
            "no_netgroup",
            "no_user",
            "not_in_netgroup",
            "pkey_only",
            "private",
            "raw",
            "sizelimit",
            "timelimit",
            "user",
            "usercategory",
            "version",
        ]
    },
    "netgroup_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "externalhost",
            "hostcategory",
            "nisdomainname",
            "no_members",
            "raw",
            "rights",
            "setattr",
            "usercategory",
            "version",
        ]
    },
    "netgroup_remove_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "host",
            "hostgroup",
            "netgroup",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "netgroup_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "version",
        ]
    },
    "otpconfig_mod": {
        "args": [
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "ipatokenhotpauthwindow",
            "ipatokenhotpsyncwindow",
            "ipatokentotpauthwindow",
            "ipatokentotpsyncwindow",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "otpconfig_show": {
        "args": [
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "otptoken_add": {
        "args": [
            "ipatokenuniqueid",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "ipatokendisabled",
            "ipatokenhotpcounter",
            "ipatokenmodel",
            "ipatokennotafter",
            "ipatokennotbefore",
            "ipatokenotpalgorithm",
            "ipatokenotpdigits",
            "ipatokenotpkey",
            "ipatokenowner",
            "ipatokenserial",
            "ipatokentotpclockoffset",
            "ipatokentotptimestep",
            "ipatokenvendor",
            "no_members",
            "no_qrcode",
            "qrcode",
            "raw",
            "setattr",
            "type",
            "version",
        ]
    },
    "otptoken_add_managedby": {
        "args": [
            "ipatokenuniqueid",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "otptoken_del": {
        "args": [
            "ipatokenuniqueid",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "otptoken_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "description",
            "ipatokendisabled",
            "ipatokenhotpcounter",
            "ipatokenmodel",
            "ipatokennotafter",
            "ipatokennotbefore",
            "ipatokenotpalgorithm",
            "ipatokenotpdigits",
            "ipatokenowner",
            "ipatokenserial",
            "ipatokentotpclockoffset",
            "ipatokentotptimestep",
            "ipatokenuniqueid",
            "ipatokenvendor",
            "no_members",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "type",
            "version",
        ]
    },
    "otptoken_mod": {
        "args": [
            "ipatokenuniqueid",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "ipatokendisabled",
            "ipatokenmodel",
            "ipatokennotafter",
            "ipatokennotbefore",
            "ipatokenowner",
            "ipatokenserial",
            "ipatokenvendor",
            "no_members",
            "raw",
            "rename",
            "rights",
            "setattr",
            "version",
        ]
    },
    "otptoken_remove_managedby": {
        "args": [
            "ipatokenuniqueid",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "otptoken_show": {
        "args": [
            "ipatokenuniqueid",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "version",
        ]
    },
    "output_find": {
        "args": [
            "commandfull_name",
            "criteria",
        ],
        "options": [
            "all",
            "pkey_only",
            "raw",
            "version",
        ]
    },
    "output_show": {
        "args": [
            "commandfull_name",
            "name",
        ],
        "options": [
            "all",
            "raw",
            "version",
        ]
    },
    "param_find": {
        "args": [
            "metaobjectfull_name",
            "criteria",
        ],
        "options": [
            "all",
            "pkey_only",
            "raw",
            "version",
        ]
    },
    "param_show": {
        "args": [
            "metaobjectfull_name",
            "name",
        ],
        "options": [
            "all",
            "raw",
            "version",
        ]
    },
    "passwd": {
        "args": [
            "principal",
            "password",
            "current_password",
        ],
        "options": [
            "otp",
            "version",
        ]
    },
    "permission_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "attrs",
            "extratargetfilter",
            "filter",
            "ipapermbindruletype",
            "ipapermlocation",
            "ipapermright",
            "ipapermtarget",
            "ipapermtargetfilter",
            "ipapermtargetfrom",
            "ipapermtargetto",
            "memberof",
            "no_members",
            "permissions",
            "raw",
            "setattr",
            "subtree",
            "targetgroup",
            "type",
            "version",
        ]
    },
    "permission_add_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "privilege",
            "raw",
            "version",
        ]
    },
    "permission_add_noaci": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "ipapermissiontype",
            "no_members",
            "raw",
            "version",
        ]
    },
    "permission_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "force",
            "version",
        ]
    },
    "permission_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "attrs",
            "cn",
            "extratargetfilter",
            "filter",
            "ipapermbindruletype",
            "ipapermdefaultattr",
            "ipapermexcludedattr",
            "ipapermincludedattr",
            "ipapermlocation",
            "ipapermright",
            "ipapermtarget",
            "ipapermtargetfilter",
            "ipapermtargetfrom",
            "ipapermtargetto",
            "memberof",
            "no_members",
            "permissions",
            "pkey_only",
            "raw",
            "sizelimit",
            "subtree",
            "targetgroup",
            "timelimit",
            "type",
            "version",
        ]
    },
    "permission_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "attrs",
            "delattr",
            "extratargetfilter",
            "filter",
            "ipapermbindruletype",
            "ipapermexcludedattr",
            "ipapermincludedattr",
            "ipapermlocation",
            "ipapermright",
            "ipapermtarget",
            "ipapermtargetfilter",
            "ipapermtargetfrom",
            "ipapermtargetto",
            "memberof",
            "no_members",
            "permissions",
            "raw",
            "rename",
            "rights",
            "setattr",
            "subtree",
            "targetgroup",
            "type",
            "version",
        ]
    },
    "permission_remove_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "privilege",
            "raw",
            "version",
        ]
    },
    "permission_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "version",
        ]
    },
    "ping": {
        "args": [
        ],
        "options": [
            "version",
        ]
    },
    "pkinit_status": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "raw",
            "server_server",
            "sizelimit",
            "status",
            "timelimit",
            "version",
        ]
    },
    "plugins": {
        "args": [
        ],
        "options": [
            "all",
            "server",
            "version",
        ]
    },
    "privilege_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "no_members",
            "raw",
            "setattr",
            "version",
        ]
    },
    "privilege_add_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "role",
            "version",
        ]
    },
    "privilege_add_permission": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "permission",
            "raw",
            "version",
        ]
    },
    "privilege_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "privilege_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "description",
            "no_members",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "privilege_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "no_members",
            "raw",
            "rename",
            "rights",
            "setattr",
            "version",
        ]
    },
    "privilege_remove_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "role",
            "version",
        ]
    },
    "privilege_remove_permission": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "permission",
            "raw",
            "version",
        ]
    },
    "privilege_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "version",
        ]
    },
    "pwpolicy_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "cospriority",
            "krbmaxpwdlife",
            "krbminpwdlife",
            "krbpwdfailurecountinterval",
            "krbpwdhistorylength",
            "krbpwdlockoutduration",
            "krbpwdmaxfailure",
            "krbpwdmindiffchars",
            "krbpwdminlength",
            "raw",
            "setattr",
            "version",
        ]
    },
    "pwpolicy_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "pwpolicy_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "cospriority",
            "krbmaxpwdlife",
            "krbminpwdlife",
            "krbpwdfailurecountinterval",
            "krbpwdhistorylength",
            "krbpwdlockoutduration",
            "krbpwdmaxfailure",
            "krbpwdmindiffchars",
            "krbpwdminlength",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "pwpolicy_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "cospriority",
            "delattr",
            "krbmaxpwdlife",
            "krbminpwdlife",
            "krbpwdfailurecountinterval",
            "krbpwdhistorylength",
            "krbpwdlockoutduration",
            "krbpwdmaxfailure",
            "krbpwdmindiffchars",
            "krbpwdminlength",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "pwpolicy_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "user",
            "version",
        ]
    },
    "radiusproxy_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "ipatokenradiusretries",
            "ipatokenradiussecret",
            "ipatokenradiusserver",
            "ipatokenradiustimeout",
            "ipatokenusermapattribute",
            "raw",
            "setattr",
            "version",
        ]
    },
    "radiusproxy_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "radiusproxy_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "description",
            "ipatokenradiusretries",
            "ipatokenradiussecret",
            "ipatokenradiusserver",
            "ipatokenradiustimeout",
            "ipatokenusermapattribute",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "radiusproxy_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "ipatokenradiusretries",
            "ipatokenradiussecret",
            "ipatokenradiusserver",
            "ipatokenradiustimeout",
            "ipatokenusermapattribute",
            "raw",
            "rename",
            "rights",
            "setattr",
            "version",
        ]
    },
    "radiusproxy_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "realmdomains_mod": {
        "args": [
        ],
        "options": [
            "add_domain",
            "addattr",
            "all",
            "associateddomain",
            "del_domain",
            "delattr",
            "force",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "realmdomains_show": {
        "args": [
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "role_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "no_members",
            "raw",
            "setattr",
            "version",
        ]
    },
    "role_add_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "service",
            "user",
            "version",
        ]
    },
    "role_add_privilege": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "privilege",
            "raw",
            "version",
        ]
    },
    "role_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "role_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "description",
            "no_members",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "role_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "no_members",
            "raw",
            "rename",
            "rights",
            "setattr",
            "version",
        ]
    },
    "role_remove_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "service",
            "user",
            "version",
        ]
    },
    "role_remove_privilege": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "privilege",
            "raw",
            "version",
        ]
    },
    "role_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "version",
        ]
    },
    "schema": {
        "args": [
        ],
        "options": [
            "known_fingerprints",
            "version",
        ]
    },
    "selfservice_add": {
        "args": [
            "aciname",
        ],
        "options": [
            "all",
            "attrs",
            "permissions",
            "raw",
            "version",
        ]
    },
    "selfservice_del": {
        "args": [
            "aciname",
        ],
        "options": [
            "version",
        ]
    },
    "selfservice_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "aciname",
            "all",
            "attrs",
            "permissions",
            "pkey_only",
            "raw",
            "version",
        ]
    },
    "selfservice_mod": {
        "args": [
            "aciname",
        ],
        "options": [
            "all",
            "attrs",
            "permissions",
            "raw",
            "version",
        ]
    },
    "selfservice_show": {
        "args": [
            "aciname",
        ],
        "options": [
            "all",
            "raw",
            "version",
        ]
    },
    "selinuxusermap_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "hostcategory",
            "ipaenabledflag",
            "ipaselinuxuser",
            "no_members",
            "raw",
            "seealso",
            "setattr",
            "usercategory",
            "version",
        ]
    },
    "selinuxusermap_add_host": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "version",
        ]
    },
    "selinuxusermap_add_user": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "selinuxusermap_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "selinuxusermap_disable": {
        "args": [
            "cn",
        ],
        "options": [
            "version",
        ]
    },
    "selinuxusermap_enable": {
        "args": [
            "cn",
        ],
        "options": [
            "version",
        ]
    },
    "selinuxusermap_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "description",
            "hostcategory",
            "ipaenabledflag",
            "ipaselinuxuser",
            "no_members",
            "pkey_only",
            "raw",
            "seealso",
            "sizelimit",
            "timelimit",
            "usercategory",
            "version",
        ]
    },
    "selinuxusermap_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "hostcategory",
            "ipaenabledflag",
            "ipaselinuxuser",
            "no_members",
            "raw",
            "rights",
            "seealso",
            "setattr",
            "usercategory",
            "version",
        ]
    },
    "selinuxusermap_remove_host": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "version",
        ]
    },
    "selinuxusermap_remove_user": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "selinuxusermap_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "version",
        ]
    },
    "server_conncheck": {
        "args": [
            "cn",
            "remote_cn",
        ],
        "options": [
            "version",
        ]
    },
    "server_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "force",
            "ignore_last_of_role",
            "ignore_topology_disconnect",
            "version",
        ]
    },
    "server_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "in_location",
            "ipamaxdomainlevel",
            "ipamindomainlevel",
            "no_members",
            "no_topologysuffix",
            "not_in_location",
            "pkey_only",
            "raw",
            "servrole",
            "sizelimit",
            "timelimit",
            "topologysuffix",
            "version",
        ]
    },
    "server_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "ipalocation_location",
            "ipaserviceweight",
            "no_members",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "server_role_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "include_master",
            "raw",
            "role_servrole",
            "server_server",
            "sizelimit",
            "status",
            "timelimit",
            "version",
        ]
    },
    "server_role_show": {
        "args": [
            "server_server",
            "role_servrole",
        ],
        "options": [
            "all",
            "raw",
            "version",
        ]
    },
    "server_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "version",
        ]
    },
    "service_add": {
        "args": [
            "krbcanonicalname",
        ],
        "options": [
            "addattr",
            "all",
            "force",
            "ipakrbauthzdata",
            "ipakrbokasdelegate",
            "ipakrboktoauthasdelegate",
            "ipakrbrequirespreauth",
            "krbprincipalauthind",
            "no_members",
            "raw",
            "setattr",
            "skip_host_check",
            "usercertificate",
            "version",
        ]
    },
    "service_add_cert": {
        "args": [
            "krbcanonicalname",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "usercertificate",
            "version",
        ]
    },
    "service_add_host": {
        "args": [
            "krbcanonicalname",
        ],
        "options": [
            "all",
            "host",
            "no_members",
            "raw",
            "version",
        ]
    },
    "service_add_principal": {
        "args": [
            "krbcanonicalname",
            "krbprincipalname",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "version",
        ]
    },
    "service_allow_create_keytab": {
        "args": [
            "krbcanonicalname",
        ],
        "options": [
            "all",
            "group",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "service_allow_retrieve_keytab": {
        "args": [
            "krbcanonicalname",
        ],
        "options": [
            "all",
            "group",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "service_del": {
        "args": [
            "krbcanonicalname",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "service_disable": {
        "args": [
            "krbcanonicalname",
        ],
        "options": [
            "version",
        ]
    },
    "service_disallow_create_keytab": {
        "args": [
            "krbcanonicalname",
        ],
        "options": [
            "all",
            "group",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "service_disallow_retrieve_keytab": {
        "args": [
            "krbcanonicalname",
        ],
        "options": [
            "all",
            "group",
            "host",
            "hostgroup",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "service_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "ipakrbauthzdata",
            "krbcanonicalname",
            "krbprincipalauthind",
            "krbprincipalname",
            "man_by_host",
            "no_members",
            "not_man_by_host",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "service_mod": {
        "args": [
            "krbcanonicalname",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "ipakrbauthzdata",
            "ipakrbokasdelegate",
            "ipakrboktoauthasdelegate",
            "ipakrbrequirespreauth",
            "krbprincipalauthind",
            "krbprincipalname",
            "no_members",
            "raw",
            "rights",
            "setattr",
            "usercertificate",
            "version",
        ]
    },
    "service_remove_cert": {
        "args": [
            "krbcanonicalname",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "usercertificate",
            "version",
        ]
    },
    "service_remove_host": {
        "args": [
            "krbcanonicalname",
        ],
        "options": [
            "all",
            "host",
            "no_members",
            "raw",
            "version",
        ]
    },
    "service_remove_principal": {
        "args": [
            "krbcanonicalname",
            "krbprincipalname",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "version",
        ]
    },
    "service_show": {
        "args": [
            "krbcanonicalname",
        ],
        "options": [
            "all",
            "no_members",
            "out",
            "raw",
            "rights",
            "version",
        ]
    },
    "servicedelegationrule_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "no_members",
            "raw",
            "setattr",
            "version",
        ]
    },
    "servicedelegationrule_add_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "principal",
            "raw",
            "version",
        ]
    },
    "servicedelegationrule_add_target": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "servicedelegationtarget",
            "version",
        ]
    },
    "servicedelegationrule_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "servicedelegationrule_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "no_members",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "servicedelegationrule_remove_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "principal",
            "raw",
            "version",
        ]
    },
    "servicedelegationrule_remove_target": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "servicedelegationtarget",
            "version",
        ]
    },
    "servicedelegationrule_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "version",
        ]
    },
    "servicedelegationtarget_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "raw",
            "setattr",
            "version",
        ]
    },
    "servicedelegationtarget_add_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "principal",
            "raw",
            "version",
        ]
    },
    "servicedelegationtarget_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "servicedelegationtarget_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "servicedelegationtarget_remove_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "principal",
            "raw",
            "version",
        ]
    },
    "servicedelegationtarget_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "session_logout": {
        "args": [
        ],
        "options": [
            "version",
        ]
    },
    "sidgen_was_run": {
        "args": [
        ],
        "options": [
            "version",
        ]
    },
    "stageuser_activate": {
        "args": [
            "uid",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "version",
        ]
    },
    "stageuser_add": {
        "args": [
            "uid",
        ],
        "options": [
            "addattr",
            "all",
            "carlicense",
            "cn",
            "departmentnumber",
            "displayname",
            "employeenumber",
            "employeetype",
            "facsimiletelephonenumber",
            "from_delete",
            "gecos",
            "gidnumber",
            "givenname",
            "homedirectory",
            "initials",
            "ipasshpubkey",
            "ipatokenradiusconfiglink",
            "ipatokenradiususername",
            "ipauserauthtype",
            "krbpasswordexpiration",
            "krbprincipalexpiration",
            "krbprincipalname",
            "l",
            "loginshell",
            "mail",
            "manager",
            "mobile",
            "no_members",
            "ou",
            "pager",
            "postalcode",
            "preferredlanguage",
            "random",
            "raw",
            "setattr",
            "sn",
            "st",
            "street",
            "telephonenumber",
            "title",
            "uidnumber",
            "usercertificate",
            "userclass",
            "userpassword",
            "version",
        ]
    },
    "stageuser_add_cert": {
        "args": [
            "uid",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "usercertificate",
            "version",
        ]
    },
    "stageuser_add_certmapdata": {
        "args": [
            "uid",
            "ipacertmapdata",
        ],
        "options": [
            "all",
            "certificate",
            "issuer",
            "no_members",
            "raw",
            "subject",
            "version",
        ]
    },
    "stageuser_add_manager": {
        "args": [
            "uid",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "stageuser_add_principal": {
        "args": [
            "uid",
            "krbprincipalname",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "version",
        ]
    },
    "stageuser_del": {
        "args": [
            "uid",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "stageuser_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "carlicense",
            "cn",
            "departmentnumber",
            "displayname",
            "employeenumber",
            "employeetype",
            "facsimiletelephonenumber",
            "gecos",
            "gidnumber",
            "givenname",
            "homedirectory",
            "in_group",
            "in_hbacrule",
            "in_netgroup",
            "in_role",
            "in_sudorule",
            "initials",
            "ipatokenradiusconfiglink",
            "ipatokenradiususername",
            "ipauserauthtype",
            "krbpasswordexpiration",
            "krbprincipalexpiration",
            "krbprincipalname",
            "l",
            "loginshell",
            "mail",
            "manager",
            "mobile",
            "no_members",
            "not_in_group",
            "not_in_hbacrule",
            "not_in_netgroup",
            "not_in_role",
            "not_in_sudorule",
            "ou",
            "pager",
            "pkey_only",
            "postalcode",
            "preferredlanguage",
            "raw",
            "sizelimit",
            "sn",
            "st",
            "street",
            "telephonenumber",
            "timelimit",
            "title",
            "uid",
            "uidnumber",
            "usercertificate",
            "userclass",
            "userpassword",
            "version",
        ]
    },
    "stageuser_mod": {
        "args": [
            "uid",
        ],
        "options": [
            "addattr",
            "all",
            "carlicense",
            "cn",
            "delattr",
            "departmentnumber",
            "displayname",
            "employeenumber",
            "employeetype",
            "facsimiletelephonenumber",
            "gecos",
            "gidnumber",
            "givenname",
            "homedirectory",
            "initials",
            "ipasshpubkey",
            "ipatokenradiusconfiglink",
            "ipatokenradiususername",
            "ipauserauthtype",
            "krbpasswordexpiration",
            "krbprincipalexpiration",
            "krbprincipalname",
            "l",
            "loginshell",
            "mail",
            "manager",
            "mobile",
            "no_members",
            "ou",
            "pager",
            "postalcode",
            "preferredlanguage",
            "random",
            "raw",
            "rename",
            "rights",
            "setattr",
            "sn",
            "st",
            "street",
            "telephonenumber",
            "title",
            "uidnumber",
            "usercertificate",
            "userclass",
            "userpassword",
            "version",
        ]
    },
    "stageuser_remove_cert": {
        "args": [
            "uid",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "usercertificate",
            "version",
        ]
    },
    "stageuser_remove_certmapdata": {
        "args": [
            "uid",
            "ipacertmapdata",
        ],
        "options": [
            "all",
            "certificate",
            "issuer",
            "no_members",
            "raw",
            "subject",
            "version",
        ]
    },
    "stageuser_remove_manager": {
        "args": [
            "uid",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "stageuser_remove_principal": {
        "args": [
            "uid",
            "krbprincipalname",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "version",
        ]
    },
    "stageuser_show": {
        "args": [
            "uid",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "version",
        ]
    },
    "sudocmd_add": {
        "args": [
            "sudocmd",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "no_members",
            "raw",
            "setattr",
            "version",
        ]
    },
    "sudocmd_del": {
        "args": [
            "sudocmd",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "sudocmd_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "description",
            "no_members",
            "pkey_only",
            "raw",
            "sizelimit",
            "sudocmd",
            "timelimit",
            "version",
        ]
    },
    "sudocmd_mod": {
        "args": [
            "sudocmd",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "no_members",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "sudocmd_show": {
        "args": [
            "sudocmd",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "version",
        ]
    },
    "sudocmdgroup_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "no_members",
            "raw",
            "setattr",
            "version",
        ]
    },
    "sudocmdgroup_add_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "sudocmd",
            "version",
        ]
    },
    "sudocmdgroup_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "sudocmdgroup_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "description",
            "no_members",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "sudocmdgroup_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "no_members",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "sudocmdgroup_remove_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "sudocmd",
            "version",
        ]
    },
    "sudocmdgroup_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "version",
        ]
    },
    "sudorule_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "cmdcategory",
            "description",
            "externalhost",
            "externaluser",
            "hostcategory",
            "ipaenabledflag",
            "ipasudorunasextgroup",
            "ipasudorunasextuser",
            "ipasudorunasgroupcategory",
            "ipasudorunasusercategory",
            "no_members",
            "raw",
            "setattr",
            "sudoorder",
            "usercategory",
            "version",
        ]
    },
    "sudorule_add_allow_command": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "sudocmd",
            "sudocmdgroup",
            "version",
        ]
    },
    "sudorule_add_deny_command": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "sudocmd",
            "sudocmdgroup",
            "version",
        ]
    },
    "sudorule_add_host": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "host",
            "hostgroup",
            "hostmask",
            "no_members",
            "raw",
            "version",
        ]
    },
    "sudorule_add_option": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "ipasudoopt",
            "no_members",
            "raw",
            "version",
        ]
    },
    "sudorule_add_runasgroup": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "no_members",
            "raw",
            "version",
        ]
    },
    "sudorule_add_runasuser": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "sudorule_add_user": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "sudorule_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "sudorule_disable": {
        "args": [
            "cn",
        ],
        "options": [
            "version",
        ]
    },
    "sudorule_enable": {
        "args": [
            "cn",
        ],
        "options": [
            "version",
        ]
    },
    "sudorule_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cmdcategory",
            "cn",
            "description",
            "externalhost",
            "externaluser",
            "hostcategory",
            "ipaenabledflag",
            "ipasudorunasextgroup",
            "ipasudorunasextuser",
            "ipasudorunasgroupcategory",
            "ipasudorunasusercategory",
            "no_members",
            "pkey_only",
            "raw",
            "sizelimit",
            "sudoorder",
            "timelimit",
            "usercategory",
            "version",
        ]
    },
    "sudorule_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "cmdcategory",
            "delattr",
            "description",
            "externalhost",
            "externaluser",
            "hostcategory",
            "ipaenabledflag",
            "ipasudorunasextgroup",
            "ipasudorunasextuser",
            "ipasudorunasgroupcategory",
            "ipasudorunasusercategory",
            "no_members",
            "raw",
            "rename",
            "rights",
            "setattr",
            "sudoorder",
            "usercategory",
            "version",
        ]
    },
    "sudorule_remove_allow_command": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "sudocmd",
            "sudocmdgroup",
            "version",
        ]
    },
    "sudorule_remove_deny_command": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "sudocmd",
            "sudocmdgroup",
            "version",
        ]
    },
    "sudorule_remove_host": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "host",
            "hostgroup",
            "hostmask",
            "no_members",
            "raw",
            "version",
        ]
    },
    "sudorule_remove_option": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "ipasudoopt",
            "no_members",
            "raw",
            "version",
        ]
    },
    "sudorule_remove_runasgroup": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "no_members",
            "raw",
            "version",
        ]
    },
    "sudorule_remove_runasuser": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "sudorule_remove_user": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "sudorule_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "version",
        ]
    },
    "topic_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "pkey_only",
            "raw",
            "version",
        ]
    },
    "topic_show": {
        "args": [
            "full_name",
        ],
        "options": [
            "all",
            "raw",
            "version",
        ]
    },
    "topologysegment_add": {
        "args": [
            "topologysuffixcn",
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "iparepltoposegmentdirection",
            "iparepltoposegmentleftnode",
            "iparepltoposegmentrightnode",
            "nsds5replicaenabled",
            "nsds5replicastripattrs",
            "nsds5replicatedattributelist",
            "nsds5replicatedattributelisttotal",
            "nsds5replicatimeout",
            "raw",
            "setattr",
            "version",
        ]
    },
    "topologysegment_del": {
        "args": [
            "topologysuffixcn",
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "topologysegment_find": {
        "args": [
            "topologysuffixcn",
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "iparepltoposegmentdirection",
            "iparepltoposegmentleftnode",
            "iparepltoposegmentrightnode",
            "nsds5replicaenabled",
            "nsds5replicastripattrs",
            "nsds5replicatedattributelist",
            "nsds5replicatedattributelisttotal",
            "nsds5replicatimeout",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "topologysegment_mod": {
        "args": [
            "topologysuffixcn",
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "nsds5replicaenabled",
            "nsds5replicastripattrs",
            "nsds5replicatedattributelist",
            "nsds5replicatedattributelisttotal",
            "nsds5replicatimeout",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "topologysegment_reinitialize": {
        "args": [
            "topologysuffixcn",
            "cn",
        ],
        "options": [
            "left",
            "right",
            "stop",
            "version",
        ]
    },
    "topologysegment_show": {
        "args": [
            "topologysuffixcn",
            "cn",
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "topologysuffix_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "iparepltopoconfroot",
            "raw",
            "setattr",
            "version",
        ]
    },
    "topologysuffix_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "topologysuffix_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "iparepltopoconfroot",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "topologysuffix_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "iparepltopoconfroot",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "topologysuffix_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "topologysuffix_verify": {
        "args": [
            "cn",
        ],
        "options": [
            "version",
        ]
    },
    "trust_add": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "base_id",
            "bidirectional",
            "external",
            "range_size",
            "range_type",
            "raw",
            "realm_admin",
            "realm_passwd",
            "realm_server",
            "setattr",
            "trust_secret",
            "trust_type",
            "version",
        ]
    },
    "trust_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "trust_fetch_domains": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "raw",
            "realm_server",
            "rights",
            "version",
        ]
    },
    "trust_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "ipantflatname",
            "ipantsidblacklistincoming",
            "ipantsidblacklistoutgoing",
            "ipanttrusteddomainsid",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "trust_mod": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "ipantadditionalsuffixes",
            "ipantsidblacklistincoming",
            "ipantsidblacklistoutgoing",
            "raw",
            "rights",
            "setattr",
            "version",
        ]
    },
    "trust_resolve": {
        "args": [
        ],
        "options": [
            "all",
            "raw",
            "sids",
            "version",
        ]
    },
    "trust_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "version",
        ]
    },
    "trustconfig_mod": {
        "args": [
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "ipantfallbackprimarygroup",
            "raw",
            "rights",
            "setattr",
            "trust_type",
            "version",
        ]
    },
    "trustconfig_show": {
        "args": [
        ],
        "options": [
            "all",
            "raw",
            "rights",
            "trust_type",
            "version",
        ]
    },
    "trustdomain_add": {
        "args": [
            "trustcn",
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "ipantflatname",
            "ipanttrusteddomainsid",
            "raw",
            "setattr",
            "trust_type",
            "version",
        ]
    },
    "trustdomain_del": {
        "args": [
            "trustcn",
            "cn",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "trustdomain_disable": {
        "args": [
            "trustcn",
            "cn",
        ],
        "options": [
            "version",
        ]
    },
    "trustdomain_enable": {
        "args": [
            "trustcn",
            "cn",
        ],
        "options": [
            "version",
        ]
    },
    "trustdomain_find": {
        "args": [
            "trustcn",
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "ipantflatname",
            "ipanttrusteddomainsid",
            "pkey_only",
            "raw",
            "sizelimit",
            "timelimit",
            "version",
        ]
    },
    "trustdomain_mod": {
        "args": [
            "trustcn",
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "ipantflatname",
            "ipanttrusteddomainsid",
            "raw",
            "rights",
            "setattr",
            "trust_type",
            "version",
        ]
    },
    "user_add": {
        "args": [
            "uid",
        ],
        "options": [
            "addattr",
            "all",
            "carlicense",
            "cn",
            "departmentnumber",
            "displayname",
            "employeenumber",
            "employeetype",
            "facsimiletelephonenumber",
            "gecos",
            "gidnumber",
            "givenname",
            "homedirectory",
            "initials",
            "ipasshpubkey",
            "ipatokenradiusconfiglink",
            "ipatokenradiususername",
            "ipauserauthtype",
            "krbpasswordexpiration",
            "krbprincipalexpiration",
            "krbprincipalname",
            "l",
            "loginshell",
            "mail",
            "manager",
            "mobile",
            "no_members",
            "noprivate",
            "nsaccountlock",
            "ou",
            "pager",
            "postalcode",
            "preferredlanguage",
            "random",
            "raw",
            "setattr",
            "sn",
            "st",
            "street",
            "telephonenumber",
            "title",
            "uidnumber",
            "usercertificate",
            "userclass",
            "userpassword",
            "version",
        ]
    },
    "user_add_cert": {
        "args": [
            "uid",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "usercertificate",
            "version",
        ]
    },
    "user_add_certmapdata": {
        "args": [
            "uid",
            "ipacertmapdata",
        ],
        "options": [
            "all",
            "certificate",
            "issuer",
            "no_members",
            "raw",
            "subject",
            "version",
        ]
    },
    "user_add_manager": {
        "args": [
            "uid",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "user_add_principal": {
        "args": [
            "uid",
            "krbprincipalname",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "version",
        ]
    },
    "user_del": {
        "args": [
            "uid",
        ],
        "options": [
            "continue",
            "preserve",
            "version",
        ]
    },
    "user_disable": {
        "args": [
            "uid",
        ],
        "options": [
            "version",
        ]
    },
    "user_enable": {
        "args": [
            "uid",
        ],
        "options": [
            "version",
        ]
    },
    "user_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "carlicense",
            "cn",
            "departmentnumber",
            "displayname",
            "employeenumber",
            "employeetype",
            "facsimiletelephonenumber",
            "gecos",
            "gidnumber",
            "givenname",
            "homedirectory",
            "in_group",
            "in_hbacrule",
            "in_netgroup",
            "in_role",
            "in_sudorule",
            "initials",
            "ipatokenradiusconfiglink",
            "ipatokenradiususername",
            "ipauserauthtype",
            "krbpasswordexpiration",
            "krbprincipalexpiration",
            "krbprincipalname",
            "l",
            "loginshell",
            "mail",
            "manager",
            "mobile",
            "no_members",
            "not_in_group",
            "not_in_hbacrule",
            "not_in_netgroup",
            "not_in_role",
            "not_in_sudorule",
            "nsaccountlock",
            "ou",
            "pager",
            "pkey_only",
            "postalcode",
            "preferredlanguage",
            "preserved",
            "raw",
            "sizelimit",
            "sn",
            "st",
            "street",
            "telephonenumber",
            "timelimit",
            "title",
            "uid",
            "uidnumber",
            "usercertificate",
            "userclass",
            "userpassword",
            "version",
            "whoami",
        ]
    },
    "user_mod": {
        "args": [
            "uid",
        ],
        "options": [
            "addattr",
            "all",
            "carlicense",
            "cn",
            "delattr",
            "departmentnumber",
            "displayname",
            "employeenumber",
            "employeetype",
            "facsimiletelephonenumber",
            "gecos",
            "gidnumber",
            "givenname",
            "homedirectory",
            "initials",
            "ipasshpubkey",
            "ipatokenradiusconfiglink",
            "ipatokenradiususername",
            "ipauserauthtype",
            "krbpasswordexpiration",
            "krbprincipalexpiration",
            "krbprincipalname",
            "l",
            "loginshell",
            "mail",
            "manager",
            "mobile",
            "no_members",
            "nsaccountlock",
            "ou",
            "pager",
            "postalcode",
            "preferredlanguage",
            "random",
            "raw",
            "rename",
            "rights",
            "setattr",
            "sn",
            "st",
            "street",
            "telephonenumber",
            "title",
            "uidnumber",
            "usercertificate",
            "userclass",
            "userpassword",
            "version",
        ]
    },
    "user_remove_cert": {
        "args": [
            "uid",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "usercertificate",
            "version",
        ]
    },
    "user_remove_certmapdata": {
        "args": [
            "uid",
            "ipacertmapdata",
        ],
        "options": [
            "all",
            "certificate",
            "issuer",
            "no_members",
            "raw",
            "subject",
            "version",
        ]
    },
    "user_remove_manager": {
        "args": [
            "uid",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "user",
            "version",
        ]
    },
    "user_remove_principal": {
        "args": [
            "uid",
            "krbprincipalname",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "version",
        ]
    },
    "user_show": {
        "args": [
            "uid",
        ],
        "options": [
            "all",
            "no_members",
            "out",
            "raw",
            "rights",
            "version",
        ]
    },
    "user_stage": {
        "args": [
            "uid",
        ],
        "options": [
            "continue",
            "version",
        ]
    },
    "user_status": {
        "args": [
            "useruid",
        ],
        "options": [
            "all",
            "raw",
            "version",
        ]
    },
    "user_undel": {
        "args": [
            "uid",
        ],
        "options": [
            "version",
        ]
    },
    "user_unlock": {
        "args": [
            "uid",
        ],
        "options": [
            "version",
        ]
    },
    "vault_add_internal": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "description",
            "ipavaultpublickey",
            "ipavaultsalt",
            "ipavaulttype",
            "no_members",
            "raw",
            "service",
            "setattr",
            "shared",
            "username",
            "version",
        ]
    },
    "vault_add_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "no_members",
            "raw",
            "service",
            "services",
            "shared",
            "user",
            "username",
            "version",
        ]
    },
    "vault_add_owner": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "no_members",
            "raw",
            "service",
            "services",
            "shared",
            "user",
            "username",
            "version",
        ]
    },
    "vault_archive_internal": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "nonce",
            "raw",
            "service",
            "session_key",
            "shared",
            "username",
            "vault_data",
            "version",
        ]
    },
    "vault_del": {
        "args": [
            "cn",
        ],
        "options": [
            "continue",
            "service",
            "shared",
            "username",
            "version",
        ]
    },
    "vault_find": {
        "args": [
            "criteria",
        ],
        "options": [
            "all",
            "cn",
            "description",
            "ipavaulttype",
            "no_members",
            "pkey_only",
            "raw",
            "service",
            "services",
            "shared",
            "sizelimit",
            "timelimit",
            "username",
            "users",
            "version",
        ]
    },
    "vault_mod_internal": {
        "args": [
            "cn",
        ],
        "options": [
            "addattr",
            "all",
            "delattr",
            "description",
            "ipavaultpublickey",
            "ipavaultsalt",
            "ipavaulttype",
            "no_members",
            "raw",
            "rights",
            "service",
            "setattr",
            "shared",
            "username",
            "version",
        ]
    },
    "vault_remove_member": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "no_members",
            "raw",
            "service",
            "services",
            "shared",
            "user",
            "username",
            "version",
        ]
    },
    "vault_remove_owner": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "group",
            "no_members",
            "raw",
            "service",
            "services",
            "shared",
            "user",
            "username",
            "version",
        ]
    },
    "vault_retrieve_internal": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "raw",
            "service",
            "session_key",
            "shared",
            "username",
            "version",
        ]
    },
    "vault_show": {
        "args": [
            "cn",
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "service",
            "shared",
            "username",
            "version",
        ]
    },
    "vaultconfig_show": {
        "args": [
        ],
        "options": [
            "all",
            "raw",
            "transport_out",
            "version",
        ]
    },
    "vaultcontainer_add_owner": {
        "args": [
        ],
        "options": [
            "all",
            "group",
            "no_members",
            "raw",
            "service",
            "services",
            "shared",
            "user",
            "username",
            "version",
        ]
    },
    "vaultcontainer_del": {
        "args": [
        ],
        "options": [
            "continue",
            "service",
            "shared",
            "username",
            "version",
        ]
    },
    "vaultcontainer_remove_owner": {
        "args": [
        ],
        "options": [
            "all",
            "group",
            "no_members",
            "raw",
            "service",
            "services",
            "shared",
            "user",
            "username",
            "version",
        ]
    },
    "vaultcontainer_show": {
        "args": [
        ],
        "options": [
            "all",
            "no_members",
            "raw",
            "rights",
            "service",
            "shared",
            "username",
            "version",
        ]
    },
}
