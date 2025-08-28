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
- Create, update, delete, or get IPv6 List Filter objects from the Verity API.
- This module interacts with the `/ipv6lists` endpoints.
module: ipv6lists
options:
  data:
    description:
    - IPv6 List Filter definition object.
    required: false
    suboptions:
      ipv6_list_filter:
        description:
        - IPv6 List Filter definition object.
        required: true
        suboptions:
          name:
            description:
            - IPv6 List Filter name.
            required: true
            suboptions:
              enable:
                default: false
                description:
                - Enable object.
                required: false
                type: bool
              ipv6_list:
                default: ''
                description:
                - Comma separated list of IPv6 addresses
                required: false
                type: str
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
short_description: Manage IPv6 List Filters via Verity API
'''

EXAMPLES = r'''- name: Create IPv6 List Filter
  be_networks.verity.ipv6lists:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      ipv6_list_filter:
        TestIPv6 List Filter:
          enable: true
          ipv6_list: ipv6_list
          name: name
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit IPv6 List Filter
  be_networks.verity.ipv6lists:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      ipv6_list_filter:
        TestIPv6 List Filter:
          enable: true
          ipv6_list: ipv6_list
          name: name
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete IPv6 List Filter
  be_networks.verity.ipv6lists:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      ipv6_list_filter_name: TestIPv6 List Filter
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the IPv6 List Filter object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "ipv6lists", "/ipv6lists")


def main():
    run_module()


if __name__ == '__main__':
    main()
