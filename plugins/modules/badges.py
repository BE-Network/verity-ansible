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
- Create, update, delete, or get Badge objects from the Verity API.
- This module interacts with the `/badges` endpoints.
module: badges
options:
  data:
    description:
    - Badge definition object.
    required: false
    suboptions:
      badge:
        description:
        - Badge definition object.
        required: true
        suboptions:
          name:
            description:
            - Badge name.
            required: true
            suboptions:
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
short_description: Manage Badges via Verity API
'''

EXAMPLES = r'''- name: Create Badge
  be_networks.verity.badges:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      badge:
        TestBadge:
          name: name
          object_properties:
            notes: notes
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Badge
  be_networks.verity.badges:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      badge:
        TestBadge:
          name: name
          object_properties:
            notes: notes
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Badge
  be_networks.verity.badges:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      badge_name: TestBadge
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Badge object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "badges", "/badges")


def main():
    run_module()


if __name__ == '__main__':
    main()
