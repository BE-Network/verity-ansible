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
- Create, update, delete, or get Community List objects from the Verity API.
- This module interacts with the `/communitylists` endpoints.
module: communitylists
options:
  data:
    description:
    - Community List definition object.
    required: false
    suboptions:
      community_list:
        description:
        - Community List definition object.
        required: true
        suboptions:
          name:
            description:
            - Community List name.
            required: true
            suboptions:
              any_all:
                choices:
                - any
                - all
                default: any
                description:
                - BGP does not advertise any or all routes that do not match the Community
                  String
                required: false
                type: str
              enable:
                default: false
                description:
                - Enable object.
                required: false
                type: bool
              lists:
                elements: dict
                suboptions:
                  community_string_expanded_expression:
                    default: ''
                    description:
                    - Community String in standard mode and Expanded Expression in
                      Expanded mode
                    required: false
                    type: str
                  enable:
                    default: false
                    description:
                    - Enable of this Community List
                    required: false
                    type: bool
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                  mode:
                    choices:
                    - no_advertise
                    - local_as
                    - no_peer_set
                    - community
                    - no_export_set
                    default: community
                    description:
                    - Mode
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
              permit_deny:
                choices:
                - permit
                - deny
                default: permit
                description:
                - Action upon match of Community Strings.
                required: false
                type: str
              standard_expanded:
                choices:
                - standard
                - expanded
                default: standard
                description:
                - Used Community String or Expanded Expression
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
short_description: Manage Community Lists via Verity API
'''

EXAMPLES = r'''- name: Create Community List
  be_networks.verity.communitylists:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      community_list:
        TestCommunity List:
          any_all: any
          enable: true
          lists:
          - community_string_expanded_expression: community_string_expanded_expression
            enable: true
            index: 1
            mode: no_advertise
          name: name
          object_properties:
            notes: notes
          permit_deny: permit
          standard_expanded: standard
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Community List
  be_networks.verity.communitylists:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      community_list:
        TestCommunity List:
          any_all: any
          enable: true
          lists:
          - community_string_expanded_expression: community_string_expanded_expression
            enable: true
            index: 1
            mode: no_advertise
          name: name
          object_properties:
            notes: notes
          permit_deny: permit
          standard_expanded: standard
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Community List
  be_networks.verity.communitylists:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      community_list_name: TestCommunity List
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Community List object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "communitylists", "/communitylists")


def main():
    run_module()


if __name__ == '__main__':
    main()
