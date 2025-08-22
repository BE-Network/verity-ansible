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
- Create, update, delete, or get SFP Breakout objects from the Verity API.
- This module interacts with the `/sfpbreakouts` endpoints.
module: sfpbreakouts
options:
  data:
    description:
    - SFP Breakout definition object.
    required: false
    suboptions:
      sfp_breakouts:
        description:
        - SFP Breakout definition object.
        required: true
        suboptions:
          name:
            description:
            - SFP Breakout name.
            required: true
            suboptions:
              breakout:
                elements: dict
                suboptions:
                  breakout:
                    choices:
                    - 8x1G
                    - 2x10G
                    - pg200G
                    - 1x50G
                    - pg100G
                    - 2x400G
                    - 8x400G
                    - 4x100G
                    - 1x40G
                    - 1x1G
                    - 2x25G
                    - pg1G
                    - 8x10G
                    - 2x40G
                    - 1x200G
                    - 2x50G
                    - 4x40G
                    - pg800G
                    - pg10G
                    - 4x50G
                    - 8x40G
                    - 8x200G
                    - 8x100G
                    - 8x50G
                    - pg40G
                    - 1x25G
                    - 2x800G
                    - 4x400G
                    - 1x10G
                    - 4x25G
                    - 4x1G
                    - 2x100G
                    - 8x800G
                    - 8x25G
                    - pg400G
                    - 1x800G
                    - 2x200G
                    - 4x200G
                    - pg25G
                    - 1x100G
                    - 2x1G
                    - 1x400G
                    - 4x10G
                    - 4x800G
                    - pg50G
                    default: 1x100G
                    description:
                    - Breakout definition; defines number of ports of what speed this
                      port is brokenout to.
                    required: false
                    type: str
                  enable:
                    default: false
                    description:
                    - Enable
                    required: false
                    type: bool
                  part_number:
                    default: ''
                    description:
                    - Part Number
                    required: false
                    type: str
                  vendor:
                    default: ''
                    description:
                    - Vendor
                    required: false
                    type: str
                type: list
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
                suboptions: {}
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
short_description: Manage SFP Breakouts via Verity API
'''

EXAMPLES = r'''- name: Create SFP Breakout
  verity.api.sfpbreakouts:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      sfp_breakouts:
        TestSFP Breakout:
          breakout:
          - breakout: 8x1G
            enable: true
            part_number: part_number
            vendor: vendor
          enable: true
          name: name
          object_properties: {}
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit SFP Breakout
  verity.api.sfpbreakouts:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      sfp_breakouts:
        TestSFP Breakout:
          breakout:
          - breakout: 8x1G
            enable: true
            part_number: part_number
            vendor: vendor
          enable: true
          name: name
          object_properties: {}
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete SFP Breakout
  verity.api.sfpbreakouts:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      sfp_breakouts_name: TestSFP Breakout
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the SFP Breakout object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "sfpbreakouts", "/sfpbreakouts")


def main():
    run_module()


if __name__ == '__main__':
    main()
