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
- Create, update, delete, or get Bundle objects from the Verity API.
- This module interacts with the `/bundles` endpoints.
module: bundles
options:
  data:
    description:
    - Bundle definition object.
    required: false
    suboptions:
      endpoint_bundle:
        description:
        - Bundle definition object.
        required: true
        suboptions:
          name:
            description:
            - Bundle name.
            required: true
            suboptions:
              cli_commands:
                default: ''
                description:
                - CLI Commands
                required: false
                type: str
              device_settings:
                default: eth_device_profile|(Device Settings)|
                description:
                - Device Settings for device
                required: false
                type: str
              device_settings_ref_type_:
                choices:
                - eth_device_profiles
                default: null
                description:
                - Object type for device_settings field
                required: false
                type: str
              eth_port_paths:
                elements: dict
                suboptions:
                  eth_port_num_eth_port_profile:
                    default: ''
                    description:
                    - Eth Port Profile Or LAG for Eth Port
                    required: false
                    type: str
                  eth_port_num_eth_port_profile_ref_type_:
                    choices:
                    - eth_port_profile_
                    - lag
                    - pb_egress_profile
                    default: null
                    description:
                    - Object type for eth_port_num_eth_port_profile field
                    required: false
                    type: str
                  eth_port_num_eth_port_settings:
                    default: ''
                    description:
                    - Choose an Eth Port Settings
                    required: false
                    type: str
                  eth_port_num_eth_port_settings_ref_type_:
                    choices:
                    - eth_port_settings
                    default: null
                    description:
                    - Object type for eth_port_num_eth_port_settings field
                    required: false
                    type: str
                  eth_port_num_gateway_profile:
                    default: ''
                    description:
                    - Gateway Profile or LAG for Eth Port
                    required: false
                    type: str
                  eth_port_num_gateway_profile_ref_type_:
                    choices:
                    - gateway_profile
                    - lag
                    default: null
                    description:
                    - Object type for eth_port_num_gateway_profile field
                    required: false
                    type: str
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                  port_name:
                    default: null
                    description:
                    - The name identifying the port. Used for reference only, it won't
                      actually change the port name.
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
                  is_for_switch:
                    default: false
                    description:
                    - Denotes a Switch Bundle
                    required: false
                    type: bool
                type: dict
              rg_services:
                elements: dict
                suboptions:
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                  row_ip_mask:
                    default: ''
                    description:
                    - IP/Mask
                    required: false
                    type: str
                type: list
              user_services:
                elements: dict
                suboptions:
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                  row_app_cli_commands:
                    default: ''
                    description:
                    - CLI Commands of this User application
                    required: false
                    type: str
                  row_app_connected_service:
                    default: ''
                    description:
                    - Service connected to this User application
                    required: false
                    type: str
                  row_app_connected_service_ref_type_:
                    choices:
                    - service
                    default: null
                    description:
                    - Object type for row_app_connected_service field
                    required: false
                    type: str
                  row_app_enable:
                    default: false
                    description:
                    - Enable of this User application
                    required: false
                    type: bool
                  row_ip_mask:
                    default: ''
                    description:
                    - IP/Mask
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
short_description: Manage Bundles via Verity API
'''

EXAMPLES = r'''- name: Create Bundle
  verity.api.bundles:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      endpoint_bundle:
        TestBundle:
          cli_commands: cli_commands
          device_settings: device_settings
          device_settings_ref_type_: eth_device_profiles
          eth_port_paths:
          - eth_port_num_eth_port_profile: eth_port_num_eth_port_profile
            eth_port_num_eth_port_profile_ref_type_: eth_port_profile_
            eth_port_num_eth_port_settings: eth_port_num_eth_port_settings
            eth_port_num_eth_port_settings_ref_type_: eth_port_settings
            eth_port_num_gateway_profile: eth_port_num_gateway_profile
            eth_port_num_gateway_profile_ref_type_: gateway_profile
            index: 1
            port_name: port_name
          name: name
          object_properties:
            is_for_switch: true
          rg_services:
          - index: 1
            row_ip_mask: row_ip_mask
          user_services:
          - index: 1
            row_app_cli_commands: row_app_cli_commands
            row_app_connected_service: row_app_connected_service
            row_app_connected_service_ref_type_: service
            row_app_enable: true
            row_ip_mask: row_ip_mask
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Bundle
  verity.api.bundles:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      endpoint_bundle:
        TestBundle:
          cli_commands: cli_commands
          device_settings: device_settings
          device_settings_ref_type_: eth_device_profiles
          eth_port_paths:
          - eth_port_num_eth_port_profile: eth_port_num_eth_port_profile
            eth_port_num_eth_port_profile_ref_type_: eth_port_profile_
            eth_port_num_eth_port_settings: eth_port_num_eth_port_settings
            eth_port_num_eth_port_settings_ref_type_: eth_port_settings
            eth_port_num_gateway_profile: eth_port_num_gateway_profile
            eth_port_num_gateway_profile_ref_type_: gateway_profile
            index: 1
            port_name: port_name
          name: name
          object_properties:
            is_for_switch: true
          rg_services:
          - index: 1
            row_ip_mask: row_ip_mask
          user_services:
          - index: 1
            row_app_cli_commands: row_app_cli_commands
            row_app_connected_service: row_app_connected_service
            row_app_connected_service_ref_type_: service
            row_app_enable: true
            row_ip_mask: row_ip_mask
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Bundle
  verity.api.bundles:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      endpoint_bundle_name: TestBundle
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Bundle object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "bundles", "/bundles")


def main():
    run_module()


if __name__ == '__main__':
    main()
