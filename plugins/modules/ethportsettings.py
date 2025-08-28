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
- Create, update, delete, or get Eth-Port Setting objects from the Verity API.
- This module interacts with the `/ethportsettings` endpoints.
module: ethportsettings
options:
  data:
    description:
    - Eth-Port Setting definition object.
    required: false
    suboptions:
      eth_port_settings:
        description:
        - Eth-Port Setting definition object.
        required: true
        suboptions:
          name:
            description:
            - Eth-Port Setting name.
            required: true
            suboptions:
              action:
                choices:
                - Protect
                - Restrict
                - Shutdown
                default: Protect
                description:
                - "Action taken if broadcast/multicast/unknown-unicast traffic excedes\
                  \ the Max. One of: <br>\n                                      \
                  \          <div class=\"tab\">\n                               \
                  \                     Protect: Broadcast/Multicast packets beyond\
                  \ the percent rate are silently dropped. QOS drop counters should\
                  \ indicate the drops.<br><br>\n                                \
                  \                    Restrict: Broadcast/Multicast packets beyond\
                  \ the percent rate are dropped. QOS drop counters should indicate\
                  \ the drops.\n                                                 \
                  \   Alarm is raised . Alarm automatically clears when rate is below\
                  \ configured threshold. <br><br>\n                             \
                  \                       Shutdown: Alarm is raised and port is taken\
                  \ out of service. User must administratively Disable and Enable\
                  \ the port to restore service. <br>\n                          \
                  \                      </div>\n                                \
                  \            "
                required: false
                type: str
              allocated_power:
                default: '0.0'
                description:
                - Power the PoE system will attempt to allocate on this port
                required: false
                type: str
              auto_negotiation:
                default: true
                description:
                - Indicates if port speed and duplex mode should be auto negotiated
                required: false
                type: bool
              bpdu_filter:
                default: false
                description:
                - Drop all Rx and Tx BPDUs
                required: false
                type: bool
              bpdu_guard:
                default: false
                description:
                - Block port on BPDU Receive
                required: false
                type: bool
              broadcast:
                default: true
                description:
                - Broadcast
                required: false
                type: bool
              bsp_enable:
                default: false
                description:
                - Enable Traffic Storm Protection which prevents excessive broadcast/multicast/unknown-unicast
                  traffic from overwhelming the Switch CPU
                required: false
                type: bool
              duplex_mode:
                choices:
                - Full
                - Auto
                - Half
                default: Auto
                description:
                - Duplex Mode
                required: false
                type: str
              enable:
                default: false
                description:
                - 'Enable object.

                  It''s highly recommended to set this value to true so that validation
                  on the object will be ran.'
                required: false
                type: bool
              enable_ecn:
                default: true
                description:
                - Enables Explicit Congestion Notification for WRED.
                required: false
                type: bool
              enable_watchdog_tuning:
                default: false
                description:
                - Enables custom tuning of Watchdog values. Uncheck to use Switch
                  default values.
                required: false
                type: bool
              enable_wred_tuning:
                default: false
                description:
                - Enables custom tuning of WRED values. Uncheck to use Switch default
                  values.
                required: false
                type: bool
              fast_learning_mode:
                default: true
                description:
                - Enable Immediate Transition to Forwarding
                required: false
                type: bool
              fec:
                choices:
                - none
                - rs
                - fc
                - unaltered
                - rs-custom
                - auto
                default: unaltered
                description:
                - "FEC is Forward Error Correction which is error correction on the\
                  \ fiber link.\n                                                <div\
                  \ class=\"tab\">\n                                             \
                  \       Any: Allows switch Negotiation between FC and RS <br>\n\
                  \                                                    None: Disables\
                  \ FEC on an interface.<br>\n                                   \
                  \                 FC: Enables FEC on supported interfaces. FC stands\
                  \ for fire code.<br>\n                                         \
                  \           RS: Enables FEC on supported interfaces. RS stands for\
                  \ Reed-Solomon code. <br>\n                                    \
                  \                None: VnetC doesn't alter the Switch Value.<br>\n\
                  \                                                </div>\n      \
                  \                                      "
                required: false
                type: str
              guard_loop:
                default: false
                description:
                - Enable Cisco Guard Loop
                required: false
                type: bool
              max_allowed_unit:
                choices:
                - pps
                - '%'
                - Kpps
                default: pps
                description:
                - "Max Percentage of the ports bandwidth allowed for broadcast/multicast/unknown-unicast\
                  \ traffic before invoking the protective action <br>\n         \
                  \                                       <div class=\"tab\">\n  \
                  \                                                  %: Percentage.<br>\n\
                  \                                                    kbps: kilobits\
                  \ per second <br>\n                                            \
                  \        mbps: megabits per second <br>\n                      \
                  \                              gbps: gigabits per second <br>\n\
                  \                                                    pps: packet\
                  \ per second <br>\n                                            \
                  \        kpps: kilopacket per second <br>\n                    \
                  \                            </div>\n                          \
                  \                      "
                required: false
                type: str
              max_allowed_value:
                default: 1000
                description:
                - Max Percentage of the ports bandwidth allowed for broadcast/multicast/unknown-unicast
                  traffic before invoking the protective action
                required: false
                type: int
              max_bit_rate:
                choices:
                - '10000'
                - '10'
                - '5000'
                - '25000'
                - '2500'
                - '50000'
                - '-1'
                - '400000'
                - '100000'
                - '1000'
                - '100'
                - '40000'
                default: '-1'
                description:
                - Maximum Bit Rate allowed
                required: false
                type: str
              maximum_wred_threshold:
                default: 1
                description:
                - A value between 1 to 12480(in KiloBytes)
                required: false
                type: int
              minimum_wred_threshold:
                default: 1
                description:
                - A value between 1 to 12480(in KiloBytes)
                required: false
                type: int
              multicast:
                default: true
                description:
                - Multicast
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
                  group:
                    default: ''
                    description:
                    - Group
                    required: false
                    type: str
                type: dict
              packet_queue:
                default: ''
                description:
                - Packet Queue
                required: false
                type: str
              packet_queue_ref_type_:
                choices:
                - packet_queue
                default: null
                description:
                - Object type for packet_queue field
                required: false
                type: str
              poe_enable:
                default: false
                description:
                - PoE Enable
                required: false
                type: bool
              priority:
                choices:
                - Critical
                - High
                - Low
                default: High
                description:
                - Priority given when assigning power in a limited power situation
                required: false
                type: str
              priority_flow_control_watchdog_action:
                choices:
                - DROP
                - FORWARD
                default: DROP
                description:
                - Ports with this setting will be disabled when link state tracking
                  takes effect
                required: false
                type: str
              priority_flow_control_watchdog_detect_time:
                default: 100
                description:
                - A value between 100 to 5000
                required: false
                type: int
              priority_flow_control_watchdog_restore_time:
                default: 100
                description:
                - A value between 100 to 60000
                required: false
                type: int
              single_link:
                default: false
                description:
                - Ports with this setting will be disabled when link state tracking
                  takes effect
                required: false
                type: bool
              stp_enable:
                default: false
                description:
                - 'Enable Spanning Tree on the port.  Note: the Spanning Tree Type
                  (VLAN, Port, MST) is controlled in the Site Settings'
                required: false
                type: bool
              wred_drop_probability:
                default: 0
                description:
                - A value between 0 to 100
                required: false
                type: int
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
short_description: Manage Eth-Port Settings via Verity API
'''

EXAMPLES = r'''- name: Create Eth-Port Setting
  be_networks.verity.ethportsettings:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      eth_port_settings:
        TestEth-Port Setting:
          action: Protect
          allocated_power: allocated_power
          auto_negotiation: true
          bpdu_filter: true
          bpdu_guard: true
          broadcast: true
          bsp_enable: true
          duplex_mode: Full
          enable: true
          enable_ecn: true
          enable_watchdog_tuning: true
          enable_wred_tuning: true
          fast_learning_mode: true
          fec: none
          guard_loop: true
          max_allowed_unit: pps
          max_allowed_value: 1
          max_bit_rate: '10000'
          maximum_wred_threshold: 1
          minimum_wred_threshold: 1
          multicast: true
          name: name
          object_properties:
            group: group
          packet_queue: packet_queue
          packet_queue_ref_type_: packet_queue
          poe_enable: true
          priority: Critical
          priority_flow_control_watchdog_action: DROP
          priority_flow_control_watchdog_detect_time: 1
          priority_flow_control_watchdog_restore_time: 1
          single_link: true
          stp_enable: true
          wred_drop_probability: 1
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Eth-Port Setting
  be_networks.verity.ethportsettings:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      eth_port_settings:
        TestEth-Port Setting:
          action: Protect
          allocated_power: allocated_power
          auto_negotiation: true
          bpdu_filter: true
          bpdu_guard: true
          broadcast: true
          bsp_enable: true
          duplex_mode: Full
          enable: true
          enable_ecn: true
          enable_watchdog_tuning: true
          enable_wred_tuning: true
          fast_learning_mode: true
          fec: none
          guard_loop: true
          max_allowed_unit: pps
          max_allowed_value: 1
          max_bit_rate: '10000'
          maximum_wred_threshold: 1
          minimum_wred_threshold: 1
          multicast: true
          name: name
          object_properties:
            group: group
          packet_queue: packet_queue
          packet_queue_ref_type_: packet_queue
          poe_enable: true
          priority: Critical
          priority_flow_control_watchdog_action: DROP
          priority_flow_control_watchdog_detect_time: 1
          priority_flow_control_watchdog_restore_time: 1
          single_link: true
          stp_enable: true
          wred_drop_probability: 1
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Eth-Port Setting
  be_networks.verity.ethportsettings:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      eth_port_settings_name: TestEth-Port Setting
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Eth-Port Setting object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "ethportsettings", "/ethportsettings")


def main():
    run_module()


if __name__ == '__main__':
    main()
