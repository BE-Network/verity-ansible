#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2025, BeyondEdge Networks <you@example.com>
# GNU General Public License v3.0+

from __future__ import absolute_import, division, print_function
__metaclass__ = type
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.be_networks.verity.plugins.module_utils.verity_resource import run_resource, MODULE_ARGS


DOCUMENTATION = r'''author:
- BeyondEdge Networks (@yourhandle)
description:
- Create, update, delete, or get IPv6 Prefix List objects from the Verity API.
- This module interacts with the `/ipv6prefixlists` endpoints.
module: ipv6prefixlists
options:
  data:
    description:
    - IPv6 Prefix List definition object.
    required: false
    suboptions:
      ipv6_prefix_list:
        description:
        - IPv6 Prefix List definition object.
        required: true
        suboptions:
          name:
            description:
            - IPv6 Prefix List name.
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
                    - Enable of this IPv6 Prefix List
                    required: false
                    type: bool
                  greater_than_equal_value:
                    default: null
                    description:
                    - 'Match IP routes with a subnet mask greater than or equal to
                      the value indicated '
                    required: false
                    type: int
                  ipv6_prefix:
                    default: ''
                    description:
                    - 'IPv6 address and subnet to match against '
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
short_description: Manage IPv6 Prefix Lists via Verity API
'''

EXAMPLES = r'''- name: Create IPv6 Prefix List
  be_networks.verity.ipv6prefixlists:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      ipv6_prefix_list:
        TestIPv6 Prefix List:
          enable: true
          lists:
          - enable: true
            greater_than_equal_value: 1
            ipv6_prefix: ipv6_prefix
            less_than_equal_value: 1
            permit_deny: permit
          name: name
          object_properties:
            notes: notes
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit IPv6 Prefix List
  be_networks.verity.ipv6prefixlists:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      ipv6_prefix_list:
        TestIPv6 Prefix List:
          enable: true
          lists:
          - enable: true
            greater_than_equal_value: 1
            ipv6_prefix: ipv6_prefix
            less_than_equal_value: 1
            permit_deny: permit
          name: name
          object_properties:
            notes: notes
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete IPv6 Prefix List
  be_networks.verity.ipv6prefixlists:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      ipv6_prefix_list_name: TestIPv6 Prefix List
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the IPv6 Prefix List object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "ipv6prefixlists", "/ipv6prefixlists")


def main():
    run_module()


if __name__ == '__main__':
    main()
