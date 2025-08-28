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
- Create, update, delete, or get AS Path Access List objects from the Verity API.
- This module interacts with the `/aspathaccesslists` endpoints.
module: aspathaccesslists
options:
  data:
    description:
    - AS Path Access List definition object.
    required: false
    suboptions:
      as_path_access_list:
        description:
        - AS Path Access List definition object.
        required: true
        suboptions:
          name:
            description:
            - AS Path Access List name.
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
                    - Enable this AS Path Access List
                    required: false
                    type: bool
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                  regular_expression:
                    default: ''
                    description:
                    - Regular Expression to match BGP Community Strings
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
short_description: Manage AS Path Access Lists via Verity API
'''

EXAMPLES = r'''- name: Create AS Path Access List
  be_networks.verity.aspathaccesslists:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      as_path_access_list:
        TestAS Path Access List:
          enable: true
          lists:
          - enable: true
            index: 1
            regular_expression: regular_expression
          name: name
          object_properties:
            notes: notes
          permit_deny: permit
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit AS Path Access List
  be_networks.verity.aspathaccesslists:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      as_path_access_list:
        TestAS Path Access List:
          enable: true
          lists:
          - enable: true
            index: 1
            regular_expression: regular_expression
          name: name
          object_properties:
            notes: notes
          permit_deny: permit
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete AS Path Access List
  be_networks.verity.aspathaccesslists:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      as_path_access_list_name: TestAS Path Access List
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the AS Path Access List object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "aspathaccesslists", "/aspathaccesslists")


def main():
    run_module()


if __name__ == '__main__':
    main()
