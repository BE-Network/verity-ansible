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
- Create, update, delete, or get Device Setting objects from the Verity API.
- This module interacts with the `/devicesettings` endpoints.
module: devicesettings
options:
  data:
    description:
    - Device Setting definition object.
    required: false
    suboptions:
      eth_device_profiles:
        description:
        - Device Setting definition object.
        required: true
        suboptions:
          name:
            description:
            - Device Setting name.
            required: true
            suboptions:
              commit_to_flash_interval:
                default: 60
                description:
                - "Frequency in minutes to write the Switch configuration to flash.\n\
                  \                                                <br>if the value\
                  \ is blank, commit will use default switch settings.\n         \
                  \                                       <br>if the value is 0, commit\
                  \ will be turned off."
                required: false
                type: int
              cut_through_switching:
                default: false
                description:
                - Enable Cut-through Switching on all Switches
                required: false
                type: bool
              disable_tcp_udp_learned_packet_acceleration:
                default: false
                description:
                - Required for AVB, PTP and Cobranet Support
                required: false
                type: bool
              enable:
                default: false
                description:
                - Enable object.
                required: false
                type: bool
              external_battery_power_available:
                default: 40
                description:
                - External Battery Power Available
                required: false
                type: int
              external_power_available:
                default: 75
                description:
                - External Power Available
                required: false
                type: int
              mode:
                choices:
                - IEEE 802.3af
                - Manual
                default: IEEE 802.3af
                description:
                - Mode
                required: false
                type: str
              name:
                default: ''
                description:
                - Object Name. Must be unique.
                required: false
                type: str
              object_properties:
                suboptions:
                  group:
                    default: ''
                    description:
                    - Group
                    required: false
                    type: str
                type: dict
              rocev2:
                default: false
                description:
                - Enable RDMA over Converged Ethernet version 2 network protocol.
                  Switches that are set to ROCE mode should already have their port
                  breakouts set up and should not have any ports configured with LAGs.
                required: false
                type: bool
              security_audit_interval:
                default: 60
                description:
                - "Frequency in minutes of rereading this Switch running configuration\
                  \ and comparing it to expected values.\n                       \
                  \                         <br>if the value is blank, audit will\
                  \ use default switch settings.\n                               \
                  \                 <br>if the value is 0, audit will be turned off.\n\
                  \                                                "
                required: false
                type: int
              usage_threshold:
                default: '0.99'
                description:
                - Usage Threshold
                required: false
                type: float
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
short_description: Manage Device Settings via Verity API
'''

EXAMPLES = r'''- name: Create Device Setting
  verity.api.devicesettings:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      eth_device_profiles:
        TestDevice Setting:
          commit_to_flash_interval: 1
          cut_through_switching: true
          disable_tcp_udp_learned_packet_acceleration: true
          enable: true
          external_battery_power_available: 1
          external_power_available: 1
          mode: IEEE 802.3af
          name: name
          object_properties:
            group: group
          rocev2: true
          security_audit_interval: 1
          usage_threshold: 1.3
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Device Setting
  verity.api.devicesettings:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      eth_device_profiles:
        TestDevice Setting:
          commit_to_flash_interval: 1
          cut_through_switching: true
          disable_tcp_udp_learned_packet_acceleration: true
          enable: true
          external_battery_power_available: 1
          external_power_available: 1
          mode: IEEE 802.3af
          name: name
          object_properties:
            group: group
          rocev2: true
          security_audit_interval: 1
          usage_threshold: 1.3
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Device Setting
  verity.api.devicesettings:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      eth_device_profiles_name: TestDevice Setting
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Device Setting object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "devicesettings", "/devicesettings")


def main():
    run_module()


if __name__ == '__main__':
    main()
