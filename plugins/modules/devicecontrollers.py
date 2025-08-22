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
- Create, update, delete, or get Device Controller objects from the Verity API.
- This module interacts with the `/devicecontrollers` endpoints.
module: devicecontrollers
options:
  data:
    description:
    - Device Controller definition object.
    required: false
    suboptions:
      device_controller:
        description:
        - Device Controller definition object.
        required: true
        suboptions:
          name:
            description:
            - Device Controller name.
            required: true
            suboptions:
              authentication_protocol:
                choices:
                - SHA
                - MD5
                default: MD5
                description:
                - Protocol
                required: false
                type: str
              cli_access_mode:
                choices:
                - SSH
                - Telnet
                default: SSH
                description:
                - CLI Access Mode
                required: false
                type: str
              comm_type:
                choices:
                - gnmi
                - snmpv2
                - snmpv3
                default: gnmi
                description:
                - Comm Type
                required: false
                type: str
              communication_mode:
                choices:
                - sonic
                - cisco_small_business_sgxxx
                - generic_advanced_snmp
                - arista_7050_series
                - generic_snmp
                - edgecore_ecs21000
                - cisco_nexus_9xxx
                - ruckus_icx7150
                - tibit_xgs_olt_sfp
                - cisco_catalyst_c3xxx
                - juniper_acx5048
                - adtran_netvanta_series
                - eltex_ltp_gpon_olt
                - hpe_aruba_2530_series
                - netgear_prosafe_series
                - microtik_routeros_telnet
                default: sonic
                description:
                - Communication Mode
                required: false
                type: str
              controller_ip_and_mask:
                default: ''
                description:
                - Controller IP and Mask
                required: false
                type: str
              enable:
                default: false
                description:
                - Enable object.
                required: false
                type: bool
              enable_password:
                default: ''
                description:
                - Enable Password - to enable privileged CLI operations
                required: false
                type: str
              enable_password_encrypted:
                default: ''
                description:
                - Enable Password - to enable privileged CLI operations
                required: false
                type: str
              gateway:
                default: ''
                description:
                - Gateway
                required: false
                type: str
              ip_source:
                choices:
                - dhcp
                - static
                default: dhcp
                description:
                - IP Source
                required: false
                type: str
              lldp_search_string:
                default: ''
                description:
                - The unique identifier associated with the managed device.
                required: false
                type: str
              located_by:
                choices:
                - Static Port
                - LLDP
                - LAG_IDL
                - LAG
                - as_site
                default: LLDP
                description:
                - Controls how the system locates this Device within its LAN
                required: false
                type: str
              managed_on_native_vlan:
                default: true
                description:
                - Managed on native VLAN
                required: false
                type: bool
              name:
                default: ''
                description:
                - Object Name. Must be unique.
                required: false
                type: str
              passphrase:
                default: ''
                description:
                - Passphrase
                required: false
                type: str
              passphrase_encrypted:
                default: ''
                description:
                - Passphrase
                required: false
                type: str
              password:
                default: ''
                description:
                - Password
                required: false
                type: str
              password_encrypted:
                default: ''
                description:
                - Password
                required: false
                type: str
              power_state:
                default: 'on'
                description:
                - Power state of Switch Controller
                required: false
                type: str
              private_password:
                default: ''
                description:
                - Password
                required: false
                type: str
              private_password_encrypted:
                default: ''
                description:
                - Password
                required: false
                type: str
              private_protocol:
                choices:
                - AES
                - DES
                default: DES
                description:
                - Protocol
                required: false
                type: str
              sdlc:
                default: ''
                description:
                - SDLC that Device Controller belongs to
                required: false
                type: str
              security_type:
                choices:
                - authPriv
                - noAuthNoPriv
                - authNoPriv
                default: noAuthNoPriv
                description:
                - Security level
                required: false
                type: str
              snmp_community_string:
                default: private
                description:
                - Comm Credentials
                required: false
                type: str
              snmpv3_username:
                default: ''
                description:
                - Username
                required: false
                type: str
              ssh_key_or_password:
                default: ''
                description:
                - SSH Key or Password
                required: false
                type: str
              ssh_key_or_password_encrypted:
                default: ''
                description:
                - SSH Key or Password
                required: false
                type: str
              switch_gateway:
                default: ''
                description:
                - Gateway of Managed Device
                required: false
                type: str
              switch_ip_and_mask:
                default: ''
                description:
                - Switch IP and Mask
                required: false
                type: str
              switchpoint:
                default: ''
                description:
                - Switchpoint reference
                required: false
                type: str
              switchpoint_ref_type_:
                choices:
                - switchpoint
                default: null
                description:
                - Object type for switchpoint field
                required: false
                type: str
              uplink_port:
                default: ''
                description:
                - Uplink Port of Managed Device
                required: false
                type: str
              username:
                default: ''
                description:
                - Username
                required: false
                type: str
              ztp_identification:
                default: ''
                description:
                - Service Tag or Serial Number to identify device for Zero Touch Provisioning
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
short_description: Manage Device Controllers via Verity API
'''

EXAMPLES = r'''- name: Create Device Controller
  verity.api.devicecontrollers:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      device_controller:
        TestDevice Controller:
          authentication_protocol: SHA
          cli_access_mode: SSH
          comm_type: gnmi
          communication_mode: sonic
          controller_ip_and_mask: controller_ip_and_mask
          enable: true
          enable_password: enable_password
          enable_password_encrypted: enable_password_encrypted
          gateway: gateway
          ip_source: dhcp
          lldp_search_string: lldp_search_string
          located_by: Static Port
          managed_on_native_vlan: true
          name: name
          passphrase: passphrase
          passphrase_encrypted: passphrase_encrypted
          password: password
          password_encrypted: password_encrypted
          power_state: power_state
          private_password: private_password
          private_password_encrypted: private_password_encrypted
          private_protocol: AES
          sdlc: sdlc
          security_type: authPriv
          snmp_community_string: snmp_community_string
          snmpv3_username: snmpv3_username
          ssh_key_or_password: ssh_key_or_password
          ssh_key_or_password_encrypted: ssh_key_or_password_encrypted
          switch_gateway: switch_gateway
          switch_ip_and_mask: switch_ip_and_mask
          switchpoint: switchpoint
          switchpoint_ref_type_: switchpoint
          uplink_port: uplink_port
          username: username
          ztp_identification: ztp_identification
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Device Controller
  verity.api.devicecontrollers:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      device_controller:
        TestDevice Controller:
          authentication_protocol: SHA
          cli_access_mode: SSH
          comm_type: gnmi
          communication_mode: sonic
          controller_ip_and_mask: controller_ip_and_mask
          enable: true
          enable_password: enable_password
          enable_password_encrypted: enable_password_encrypted
          gateway: gateway
          ip_source: dhcp
          lldp_search_string: lldp_search_string
          located_by: Static Port
          managed_on_native_vlan: true
          name: name
          passphrase: passphrase
          passphrase_encrypted: passphrase_encrypted
          password: password
          password_encrypted: password_encrypted
          power_state: power_state
          private_password: private_password
          private_password_encrypted: private_password_encrypted
          private_protocol: AES
          sdlc: sdlc
          security_type: authPriv
          snmp_community_string: snmp_community_string
          snmpv3_username: snmpv3_username
          ssh_key_or_password: ssh_key_or_password
          ssh_key_or_password_encrypted: ssh_key_or_password_encrypted
          switch_gateway: switch_gateway
          switch_ip_and_mask: switch_ip_and_mask
          switchpoint: switchpoint
          switchpoint_ref_type_: switchpoint
          uplink_port: uplink_port
          username: username
          ztp_identification: ztp_identification
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Device Controller
  verity.api.devicecontrollers:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      device_controller_name: TestDevice Controller
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Device Controller object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "devicecontrollers", "/devicecontrollers")


def main():
    run_module()


if __name__ == '__main__':
    main()
