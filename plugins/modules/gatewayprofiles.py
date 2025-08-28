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
- Create, update, delete, or get Gateway Profile objects from the Verity API.
- This module interacts with the `/gatewayprofiles` endpoints.
module: gatewayprofiles
options:
  data:
    description:
    - Gateway Profile definition object.
    required: false
    suboptions:
      gateway_profile:
        description:
        - Gateway Profile definition object.
        required: true
        suboptions:
          name:
            description:
            - Gateway Profile name.
            required: true
            suboptions:
              enable:
                default: false
                description:
                - 'Enable object.

                  It''s highly recommended to set this value to true so that validation
                  on the object will be ran.'
                required: false
                type: bool
              external_gateways:
                elements: dict
                suboptions:
                  enable:
                    default: false
                    description:
                    - Enable row
                    required: false
                    type: bool
                  gateway:
                    default: ''
                    description:
                    - BGP Gateway referenced for port profile
                    required: false
                    type: str
                  gateway_ref_type_:
                    choices:
                    - gateway
                    default: null
                    description:
                    - Object type for gateway field
                    required: false
                    type: str
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                  peer_gw:
                    default: false
                    description:
                    - Setting for paired switches only. Flag indicating that this
                      gateway is a peer gateway. For each gateway profile referencing
                      a BGP session on a member of a leaf pair, the peer should have
                      a gateway profile entry indicating the IP address for the peers
                      gateway.
                    required: false
                    type: bool
                  source_ip_mask:
                    default: ''
                    description:
                    - 'Source address on the port if untagged or on the VLAN if tagged
                      used for the outgoing BGP session '
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
                  group:
                    default: ''
                    description:
                    - Group
                    required: false
                    type: str
                type: dict
              tenant_slice_managed:
                default: false
                description:
                - Profiles that Tenant Slice creates and manages
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
short_description: Manage Gateway Profiles via Verity API
'''

EXAMPLES = r'''- name: Create Gateway Profile
  be_networks.verity.gatewayprofiles:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      gateway_profile:
        TestGateway Profile:
          enable: true
          external_gateways:
          - enable: true
            gateway: gateway
            gateway_ref_type_: gateway
            index: 1
            peer_gw: true
            source_ip_mask: source_ip_mask
          name: name
          object_properties:
            group: group
          tenant_slice_managed: true
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Gateway Profile
  be_networks.verity.gatewayprofiles:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      gateway_profile:
        TestGateway Profile:
          enable: true
          external_gateways:
          - enable: true
            gateway: gateway
            gateway_ref_type_: gateway
            index: 1
            peer_gw: true
            source_ip_mask: source_ip_mask
          name: name
          object_properties:
            group: group
          tenant_slice_managed: true
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Gateway Profile
  be_networks.verity.gatewayprofiles:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      gateway_profile_name: TestGateway Profile
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Gateway Profile object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "gatewayprofiles", "/gatewayprofiles")


def main():
    run_module()


if __name__ == '__main__':
    main()
