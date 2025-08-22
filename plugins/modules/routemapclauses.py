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
- Create, update, delete, or get Route Map Clause objects from the Verity API.
- This module interacts with the `/routemapclauses` endpoints.
module: routemapclauses
options:
  data:
    description:
    - Route Map Clause definition object.
    required: false
    suboptions:
      route_map_clause:
        description:
        - Route Map Clause definition object.
        required: true
        suboptions:
          name:
            description:
            - Route Map Clause name.
            required: true
            suboptions:
              enable:
                default: false
                description:
                - Enable flag of this provisioning object
                required: false
                type: bool
              match_as_path_access_list:
                default: ''
                description:
                - Match AS Path Access List
                required: false
                type: str
              match_as_path_access_list_ref_type_:
                choices:
                - as_path_access_list
                default: null
                description:
                - Object type for match_as_path_access_list field
                required: false
                type: str
              match_community_list:
                default: ''
                description:
                - Match Community List
                required: false
                type: str
              match_community_list_ref_type_:
                choices:
                - community_list
                default: null
                description:
                - Object type for match_community_list field
                required: false
                type: str
              match_evpn_route_type:
                choices:
                - ''
                - macip
                - multicast
                - prefix
                default: ''
                description:
                - Match based on the indicated EVPN Route Type
                required: false
                type: str
              match_evpn_route_type_default:
                default: null
                description:
                - Match based on the type of EVPN Route Type being Default"
                required: false
                type: bool
              match_extended_community_list:
                default: ''
                description:
                - Match Extended Community List
                required: false
                type: str
              match_extended_community_list_ref_type_:
                choices:
                - extended_community_list
                default: null
                description:
                - Object type for match_extended_community_list field
                required: false
                type: str
              match_interface_number:
                default: null
                description:
                - Match Interface Number
                required: false
                type: int
              match_interface_vlan:
                default: null
                description:
                - Match Interface VLAN
                required: false
                type: int
              match_ipv4_address_ip_prefix_list:
                default: ''
                description:
                - Match IPv4 Address IPv4 Prefix List
                required: false
                type: str
              match_ipv4_address_ip_prefix_list_ref_type_:
                choices:
                - ipv4_prefix_list
                default: null
                description:
                - Object type for match_ipv4_address_ip_prefix_list field
                required: false
                type: str
              match_ipv4_next_hop_ip_prefix_list:
                default: ''
                description:
                - Match IPv4 Next Hop IPv4 Prefix List
                required: false
                type: str
              match_ipv4_next_hop_ip_prefix_list_ref_type_:
                choices:
                - ipv4_prefix_list
                default: null
                description:
                - Object type for match_ipv4_next_hop_ip_prefix_list field
                required: false
                type: str
              match_ipv6_address_ipv6_prefix_list:
                default: ''
                description:
                - Match IPv4 Address IPv6 Prefix List
                required: false
                type: str
              match_ipv6_address_ipv6_prefix_list_ref_type_:
                choices:
                - ipv6_prefix_list
                default: null
                description:
                - Object type for match_ipv6_address_ipv6_prefix_list field
                required: false
                type: str
              match_ipv6_next_hop_ipv6_prefix_list:
                default: ''
                description:
                - Match IPv6 Next Hop IPv6 Prefix List
                required: false
                type: str
              match_ipv6_next_hop_ipv6_prefix_list_ref_type_:
                choices:
                - ipv6_prefix_list
                default: null
                description:
                - Object type for match_ipv6_next_hop_ipv6_prefix_list field
                required: false
                type: str
              match_local_preference:
                default: null
                description:
                - 'Match BGP Local Preference value on the route '
                required: false
                type: int
              match_metric:
                default: null
                description:
                - 'Match Metric of the IP route entry '
                required: false
                type: int
              match_origin:
                choices:
                - ''
                - egp
                - igp
                - incomplete
                default: ''
                description:
                - 'Match routes based on the value of the BGP Origin attribute '
                required: false
                type: str
              match_peer_interface:
                default: null
                description:
                - 'Match BGP Peer port the route was learned from '
                required: false
                type: int
              match_peer_ip_address:
                default: ''
                description:
                - 'Match BGP Peer IP Address the route was learned from '
                required: false
                type: str
              match_peer_vlan:
                default: null
                description:
                - 'Match BGP Peer VLAN over which the route was learned '
                required: false
                type: int
              match_source_protocol:
                choices:
                - ''
                - bgp
                - connected
                - ospf
                - static
                default: ''
                description:
                - 'Match Routing  Protocol the route originated from '
                required: false
                type: str
              match_tag:
                default: null
                description:
                - Match routes that have this value for a Tag attribute
                required: false
                type: int
              match_vni:
                default: null
                description:
                - 'Match based on the VNI value '
                required: false
                type: int
              match_vrf:
                default: ''
                description:
                - 'Match VRF the route is associated with '
                required: false
                type: str
              match_vrf_ref_type_:
                choices:
                - tenant
                default: null
                description:
                - Object type for match_vrf field
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
                  match_fields_shown:
                    default: ''
                    description:
                    - Match fields shown
                    required: false
                    type: str
                  notes:
                    default: ''
                    description:
                    - User Notes.
                    required: false
                    type: str
                type: dict
              permit_deny:
                choices:
                - permit
                - deny
                default: permit
                description:
                - Action upon match of Community Strings.
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
short_description: Manage Route Map Clauses via Verity API
'''

EXAMPLES = r'''- name: Create Route Map Clause
  verity.api.routemapclauses:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      route_map_clause:
        TestRoute Map Clause:
          enable: true
          match_as_path_access_list: match_as_path_access_list
          match_as_path_access_list_ref_type_: as_path_access_list
          match_community_list: match_community_list
          match_community_list_ref_type_: community_list
          match_evpn_route_type: ''
          match_evpn_route_type_default: true
          match_extended_community_list: match_extended_community_list
          match_extended_community_list_ref_type_: extended_community_list
          match_interface_number: 1
          match_interface_vlan: 1
          match_ipv4_address_ip_prefix_list: match_ipv4_address_ip_prefix_list
          match_ipv4_address_ip_prefix_list_ref_type_: ipv4_prefix_list
          match_ipv4_next_hop_ip_prefix_list: match_ipv4_next_hop_ip_prefix_list
          match_ipv4_next_hop_ip_prefix_list_ref_type_: ipv4_prefix_list
          match_ipv6_address_ipv6_prefix_list: match_ipv6_address_ipv6_prefix_list
          match_ipv6_address_ipv6_prefix_list_ref_type_: ipv6_prefix_list
          match_ipv6_next_hop_ipv6_prefix_list: match_ipv6_next_hop_ipv6_prefix_list
          match_ipv6_next_hop_ipv6_prefix_list_ref_type_: ipv6_prefix_list
          match_local_preference: 1
          match_metric: 1
          match_origin: ''
          match_peer_interface: 1
          match_peer_ip_address: match_peer_ip_address
          match_peer_vlan: 1
          match_source_protocol: ''
          match_tag: 1
          match_vni: 1
          match_vrf: match_vrf
          match_vrf_ref_type_: tenant
          name: name
          object_properties:
            match_fields_shown: match_fields_shown
            notes: notes
          permit_deny: permit
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Route Map Clause
  verity.api.routemapclauses:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      route_map_clause:
        TestRoute Map Clause:
          enable: true
          match_as_path_access_list: match_as_path_access_list
          match_as_path_access_list_ref_type_: as_path_access_list
          match_community_list: match_community_list
          match_community_list_ref_type_: community_list
          match_evpn_route_type: ''
          match_evpn_route_type_default: true
          match_extended_community_list: match_extended_community_list
          match_extended_community_list_ref_type_: extended_community_list
          match_interface_number: 1
          match_interface_vlan: 1
          match_ipv4_address_ip_prefix_list: match_ipv4_address_ip_prefix_list
          match_ipv4_address_ip_prefix_list_ref_type_: ipv4_prefix_list
          match_ipv4_next_hop_ip_prefix_list: match_ipv4_next_hop_ip_prefix_list
          match_ipv4_next_hop_ip_prefix_list_ref_type_: ipv4_prefix_list
          match_ipv6_address_ipv6_prefix_list: match_ipv6_address_ipv6_prefix_list
          match_ipv6_address_ipv6_prefix_list_ref_type_: ipv6_prefix_list
          match_ipv6_next_hop_ipv6_prefix_list: match_ipv6_next_hop_ipv6_prefix_list
          match_ipv6_next_hop_ipv6_prefix_list_ref_type_: ipv6_prefix_list
          match_local_preference: 1
          match_metric: 1
          match_origin: ''
          match_peer_interface: 1
          match_peer_ip_address: match_peer_ip_address
          match_peer_vlan: 1
          match_source_protocol: ''
          match_tag: 1
          match_vni: 1
          match_vrf: match_vrf
          match_vrf_ref_type_: tenant
          name: name
          object_properties:
            match_fields_shown: match_fields_shown
            notes: notes
          permit_deny: permit
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Route Map Clause
  verity.api.routemapclauses:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      route_map_clause_name: TestRoute Map Clause
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Route Map Clause object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "routemapclauses", "/routemapclauses")


def main():
    run_module()


if __name__ == '__main__':
    main()
