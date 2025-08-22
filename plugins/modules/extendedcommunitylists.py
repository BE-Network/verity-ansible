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
- Create, update, delete, or get Extended Community List objects from the Verity API.
- This module interacts with the `/extendedcommunitylists` endpoints.
module: extendedcommunitylists
options:
  data:
    description:
    - Extended Community List definition object.
    required: false
    suboptions:
      extended_community_list:
        description:
        - Extended Community List definition object.
        required: true
        suboptions:
          name:
            description:
            - Extended Community List name.
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
                  enable:
                    default: false
                    description:
                    - Enable of this Extended Community List
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
                    - route
                    - soo
                    default: route
                    description:
                    - Mode
                    required: false
                    type: str
                  route_target_expanded_expression:
                    default: ''
                    description:
                    - Match against a BGP extended community of type Route Target
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
short_description: Manage Extended Community Lists via Verity API
'''

EXAMPLES = r'''- name: Create Extended Community List
  verity.api.extendedcommunitylists:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      extended_community_list:
        TestExtended Community List:
          any_all: any
          enable: true
          lists:
          - enable: true
            index: 1
            mode: route
            route_target_expanded_expression: route_target_expanded_expression
          name: name
          object_properties:
            notes: notes
          permit_deny: permit
          standard_expanded: standard
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Extended Community List
  verity.api.extendedcommunitylists:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      extended_community_list:
        TestExtended Community List:
          any_all: any
          enable: true
          lists:
          - enable: true
            index: 1
            mode: route
            route_target_expanded_expression: route_target_expanded_expression
          name: name
          object_properties:
            notes: notes
          permit_deny: permit
          standard_expanded: standard
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Extended Community List
  verity.api.extendedcommunitylists:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      extended_community_list_name: TestExtended Community List
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Extended Community List object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "extendedcommunitylists", "/extendedcommunitylists")


def main():
    run_module()


if __name__ == '__main__':
    main()
