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
- Create, update, delete, or get Pod objects from the Verity API.
- This module interacts with the `/pods` endpoints.
module: pods
options:
  data:
    description:
    - Pod definition object.
    required: false
    suboptions:
      pod:
        description:
        - Pod definition object.
        required: true
        suboptions:
          name:
            description:
            - Pod name.
            required: true
            suboptions:
              enable:
                default: true
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
short_description: Manage Pods via Verity API
'''

EXAMPLES = r'''- name: Create Pod
  be_networks.verity.pods:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      pod:
        TestPod:
          enable: true
          name: name
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Pod
  be_networks.verity.pods:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      pod:
        TestPod:
          enable: true
          name: name
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Pod
  be_networks.verity.pods:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      pod_name: TestPod
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Pod object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "pods", "/pods")


def main():
    run_module()


if __name__ == '__main__':
    main()
