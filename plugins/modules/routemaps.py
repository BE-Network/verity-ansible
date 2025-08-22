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
- Create, update, delete, or get Route Map objects from the Verity API.
- This module interacts with the `/routemaps` endpoints.
module: routemaps
options:
  data:
    description:
    - Route Map definition object.
    required: false
    suboptions:
      route_map:
        description:
        - Route Map definition object.
        required: true
        suboptions:
          name:
            description:
            - Route Map name.
            required: true
            suboptions:
              enable:
                default: false
                description:
                - Enable object.
                required: false
                type: bool
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
              route_map_clauses:
                elements: dict
                suboptions:
                  enable:
                    default: false
                    description:
                    - Enable
                    required: false
                    type: bool
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                  route_map_clause:
                    default: ''
                    description:
                    - Route Map Clause is a collection match and set rules
                    required: false
                    type: str
                  route_map_clause_ref_type_:
                    choices:
                    - route_map_clause
                    default: null
                    description:
                    - Object type for route_map_clause field
                    required: false
                    type: str
                type: list
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
short_description: Manage Route Maps via Verity API
'''

EXAMPLES = r'''- name: Create Route Map
  verity.api.routemaps:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      route_map:
        TestRoute Map:
          enable: true
          name: name
          object_properties:
            notes: notes
          route_map_clauses:
          - enable: true
            index: 1
            route_map_clause: route_map_clause
            route_map_clause_ref_type_: route_map_clause
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Route Map
  verity.api.routemaps:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      route_map:
        TestRoute Map:
          enable: true
          name: name
          object_properties:
            notes: notes
          route_map_clauses:
          - enable: true
            index: 1
            route_map_clause: route_map_clause
            route_map_clause_ref_type_: route_map_clause
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Route Map
  verity.api.routemaps:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      route_map_name: TestRoute Map
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Route Map object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "routemaps", "/routemaps")


def main():
    run_module()


if __name__ == '__main__':
    main()
