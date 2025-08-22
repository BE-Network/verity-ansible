#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2025, BeyondEdge Networks <you@example.com>
# GNU General Public License v3.0+

from __future__ import absolute_import, division, print_function
__metaclass__ = type
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.verity.api.plugins.module_utils.verity_resource import run_resource, MODULE_ARGS


DOCUMENTATION = r'''author:
- BeyondEdge Networks (@yourhandle)
description:
- Create, update, delete, or get Port ACL objects from the Verity API.
- This module interacts with the `/portacls` endpoints.
module: portacls
options:
  data:
    description:
    - Port ACL definition object.
    required: false
    suboptions:
      port_acl:
        description:
        - Port ACL definition object.
        required: true
        suboptions:
          name:
            description:
            - Port ACL name.
            required: true
            suboptions:
              enable:
                default: false
                description:
                - Enable object.
                required: false
                type: bool
              ipv4_deny:
                elements: dict
                suboptions:
                  enable:
                    default: false
                    description:
                    - Enable
                    required: false
                    type: bool
                  filter:
                    default: ''
                    description:
                    - Filter
                    required: false
                    type: str
                  filter_ref_type_:
                    choices:
                    - ipv4_filter
                    default: null
                    description:
                    - Object type for filter field
                    required: false
                    type: str
                type: list
              ipv4_permit:
                elements: dict
                suboptions:
                  enable:
                    default: false
                    description:
                    - Enable
                    required: false
                    type: bool
                  filter:
                    default: ''
                    description:
                    - Filter
                    required: false
                    type: str
                  filter_ref_type_:
                    choices:
                    - ipv4_filter
                    default: null
                    description:
                    - Object type for filter field
                    required: false
                    type: str
                type: list
              ipv6_deny:
                elements: dict
                suboptions:
                  enable:
                    default: false
                    description:
                    - Enable
                    required: false
                    type: bool
                  filter:
                    default: ''
                    description:
                    - Filter
                    required: false
                    type: str
                  filter_ref_type_:
                    choices:
                    - ipv6_filter
                    default: null
                    description:
                    - Object type for filter field
                    required: false
                    type: str
                type: list
              ipv6_permit:
                elements: dict
                suboptions:
                  enable:
                    default: false
                    description:
                    - Enable
                    required: false
                    type: bool
                  filter:
                    default: ''
                    description:
                    - Filter
                    required: false
                    type: str
                  filter_ref_type_:
                    choices:
                    - ipv6_filter
                    default: null
                    description:
                    - Object type for filter field
                    required: false
                    type: str
                type: list
              name:
                default: ''
                description:
                - Object Name. Must be unique.
                required: false
                type: str
            type: str
        type: dict
    type: dict
  params:
    description:
    - Optional parameters.
    required: false
    suboptions:
      changeset_name:
        description:
        - Changeset name
        required: false
        type: str
    type: dict
short_description: Manage Port ACLs via Verity API
'''

EXAMPLES = r'''- name: Create Port ACL
  verity.api.portacls:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      port_acl:
        TestPort ACL:
          enable: true
          ipv4_deny:
          - enable: true
            filter: filter
            filter_ref_type_: ipv4_filter
          ipv4_permit:
          - enable: true
            filter: filter
            filter_ref_type_: ipv4_filter
          ipv6_deny:
          - enable: true
            filter: filter
            filter_ref_type_: ipv6_filter
          ipv6_permit:
          - enable: true
            filter: filter
            filter_ref_type_: ipv6_filter
          name: name
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Port ACL
  verity.api.portacls:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      port_acl:
        TestPort ACL:
          enable: true
          ipv4_deny:
          - enable: true
            filter: filter
            filter_ref_type_: ipv4_filter
          ipv4_permit:
          - enable: true
            filter: filter
            filter_ref_type_: ipv4_filter
          ipv6_deny:
          - enable: true
            filter: filter
            filter_ref_type_: ipv6_filter
          ipv6_permit:
          - enable: true
            filter: filter
            filter_ref_type_: ipv6_filter
          name: name
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Port ACL
  verity.api.portacls:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      port_acl_name: TestPort ACL
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Port ACL object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "portacls", "/portacls")


def main():
    run_module()


if __name__ == '__main__':
    main()
