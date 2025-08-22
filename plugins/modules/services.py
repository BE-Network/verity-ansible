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
- Create, update, delete, or get Service objects from the Verity API.
- This module interacts with the `/services` endpoints.
module: services
options:
  data:
    description:
    - Service definition object.
    required: false
    suboptions:
      service:
        description:
        - Service definition object.
        required: true
        suboptions:
          name:
            description:
            - Service name.
            required: true
            suboptions:
              anycast_ipv4_mask:
                default: ''
                description:
                - 'Comma separated list of Static anycast gateway addresses(IPv4)
                  for service '
                required: false
                type: str
              anycast_ipv6_mask:
                default: ''
                description:
                - 'Comma separated list of Static anycast gateway addresses(IPv6)
                  for service '
                required: false
                type: str
              dhcp_server_ipv4:
                default: ''
                description:
                - IPv4 address(s) of the DHCP server for service.  May have up to
                  four separated by commas.
                required: false
                type: str
              dhcp_server_ipv6:
                default: ''
                description:
                - IPv6 address(s) of the DHCP server for service.  May have up to
                  four separated by commas.
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
              mtu:
                default: 1500
                description:
                - MTU (Maximum Transmission Unit) The size used by a switch to determine
                  when large packets must be broken up into smaller packets for delivery.
                  If mismatched within a single vlan network, can cause dropped packets.
                required: false
                type: int
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
              tenant:
                default: ''
                description:
                - Tenant
                required: false
                type: str
              tenant_ref_type_:
                choices:
                - tenant
                default: null
                description:
                - Object type for tenant field
                required: false
                type: str
              vlan:
                default: null
                description:
                - A Value between 1 and 4096
                required: false
                type: int
              vni:
                default: null
                description:
                - Indication of the outgoing VLAN layer 2 service
                required: false
                type: int
              vni_auto_assigned_:
                default: null
                description:
                - Whether or not the value in vni field has been automatically assigned
                  or not. Set to false and change vni value to edit.
                required: false
                type: bool
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
short_description: Manage Services via Verity API
'''

EXAMPLES = r'''- name: Create Service
  verity.api.services:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      service:
        TestService:
          anycast_ipv4_mask: anycast_ipv4_mask
          anycast_ipv6_mask: anycast_ipv6_mask
          dhcp_server_ipv4: dhcp_server_ipv4
          dhcp_server_ipv6: dhcp_server_ipv6
          enable: true
          mtu: 1
          name: name
          object_properties:
            group: group
          tenant: tenant
          tenant_ref_type_: tenant
          vlan: 1
          vni: 1
          vni_auto_assigned_: true
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Service
  verity.api.services:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      service:
        TestService:
          anycast_ipv4_mask: anycast_ipv4_mask
          anycast_ipv6_mask: anycast_ipv6_mask
          dhcp_server_ipv4: dhcp_server_ipv4
          dhcp_server_ipv6: dhcp_server_ipv6
          enable: true
          mtu: 1
          name: name
          object_properties:
            group: group
          tenant: tenant
          tenant_ref_type_: tenant
          vlan: 1
          vni: 1
          vni_auto_assigned_: true
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Service
  verity.api.services:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      service_name: TestService
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Service object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "services", "/services")


def main():
    run_module()


if __name__ == '__main__':
    main()
