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
- Create, update, delete, or get IPv4 Prefix List objects from the Verity API.
- This module interacts with the `/ipv4prefixlists` endpoints.
module: ipv4prefixlists
options:
  data:
    description:
    - IPv4 Prefix List definition object.
    required: false
    suboptions:
      ipv4_prefix_list:
        description:
        - IPv4 Prefix List definition object.
        required: true
        suboptions:
          name:
            description:
            - IPv4 Prefix List name.
            required: true
            suboptions:
              enable:
                default: false
                description:
                - Enable object.
                required: false
                type: bool
              lists:
                elements: dict
                suboptions:
                  enable:
                    default: false
                    description:
                    - Enable of this IPv4 Prefix List
                    required: false
                    type: bool
                  greater_than_equal_value:
                    default: null
                    description:
                    - 'Match IP routes with a subnet mask greater than or equal to
                      the value indicated '
                    required: false
                    type: int
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                  ipv4_prefix:
                    default: ''
                    description:
                    - 'IPv4 address and subnet to match against '
                    required: false
                    type: str
                  less_than_equal_value:
                    default: null
                    description:
                    - Match IP routes with a subnet mask less than or equal to the
                      value indicated
                    required: false
                    type: int
                  permit_deny:
                    choices:
                    - permit
                    - deny
                    default: permit
                    description:
                    - Action upon match of Community Strings.
                    required: false
                    type: str
                type: list
              name:
                default: ''
                description:
                - Object Name. Must be unique.
                required: false
                type: str
              object_properties:
                suboptions:
                  notes:
                    default: ''
                    description:
                    - User Notes.
                    required: false
                    type: str
                type: dict
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
short_description: Manage IPv4 Prefix Lists via Verity API
'''

EXAMPLES = r'''- name: Create IPv4 Prefix List
  verity.api.ipv4prefixlists:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      ipv4_prefix_list:
        TestIPv4 Prefix List:
          enable: true
          lists:
          - enable: true
            greater_than_equal_value: 1
            index: 1
            ipv4_prefix: ipv4_prefix
            less_than_equal_value: 1
            permit_deny: permit
          name: name
          object_properties:
            notes: notes
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit IPv4 Prefix List
  verity.api.ipv4prefixlists:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      ipv4_prefix_list:
        TestIPv4 Prefix List:
          enable: true
          lists:
          - enable: true
            greater_than_equal_value: 1
            index: 1
            ipv4_prefix: ipv4_prefix
            less_than_equal_value: 1
            permit_deny: permit
          name: name
          object_properties:
            notes: notes
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete IPv4 Prefix List
  verity.api.ipv4prefixlists:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      ipv4_prefix_list_name: TestIPv4 Prefix List
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the IPv4 Prefix List object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "ipv4prefixlists", "/ipv4prefixlists")


def main():
    run_module()


if __name__ == '__main__':
    main()
