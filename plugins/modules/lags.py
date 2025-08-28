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
- Create, update, delete, or get LAG objects from the Verity API.
- This module interacts with the `/lags` endpoints.
module: lags
options:
  data:
    description:
    - LAG definition object.
    required: false
    suboptions:
      lag:
        description:
        - LAG definition object.
        required: true
        suboptions:
          name:
            description:
            - LAG name.
            required: true
            suboptions:
              color:
                choices:
                - anakiwa
                - chardonnay
                - lavender
                - cornflower
                - emerald
                - starship
                default: anakiwa
                description:
                - Choose the color to display the connectors on the network view
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
              eth_port_profile:
                default: ''
                description:
                - Choose an Eth Port Profile
                required: false
                type: str
              eth_port_profile_ref_type_:
                choices:
                - eth_port_profile_
                - gateway_profile
                - pb_egress_profile
                default: null
                description:
                - Object type for eth_port_profile field
                required: false
                type: str
              fallback:
                default: false
                description:
                - Allows an active member interface to establish a connection with
                  a peer interface before the port channel receives the LACP protocol
                  negotiation from the peer.
                required: false
                type: bool
              fast_rate:
                default: false
                description:
                - Send LACP packets every second (if disabled, packets are sent every
                  30 seconds)
                required: false
                type: bool
              is_peer_link:
                choices:
                - true
                - false
                default: false
                description:
                - Indicates this LAG is used for peer-to-peer Peer-LAG/IDS link
                required: false
                type: bool
              lacp:
                default: true
                description:
                - LACP
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
              peer_link_vlan:
                default: null
                description:
                - For peer-peer LAGs. The VLAN used for control
                required: false
                type: int
              uplink:
                default: false
                description:
                - Indicates this LAG is designated as an uplink in the case of a spineless
                  pod. Link State Tracking will be applied to BGP Egress VLANs/Interfaces
                  and the MCLAG Peer Link VLAN
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
short_description: Manage LAGs via Verity API
'''

EXAMPLES = r'''- name: Create LAG
  be_networks.verity.lags:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      lag:
        TestLAG:
          color: anakiwa
          enable: true
          eth_port_profile: eth_port_profile
          eth_port_profile_ref_type_: eth_port_profile_
          fallback: true
          fast_rate: true
          is_peer_link: true
          lacp: true
          name: name
          object_properties: {}
          peer_link_vlan: 1
          uplink: true
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit LAG
  be_networks.verity.lags:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      lag:
        TestLAG:
          color: anakiwa
          enable: true
          eth_port_profile: eth_port_profile
          eth_port_profile_ref_type_: eth_port_profile_
          fallback: true
          fast_rate: true
          is_peer_link: true
          lacp: true
          name: name
          object_properties: {}
          peer_link_vlan: 1
          uplink: true
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete LAG
  be_networks.verity.lags:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      lag_name: TestLAG
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the LAG object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "lags", "/lags")


def main():
    run_module()


if __name__ == '__main__':
    main()
