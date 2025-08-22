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
- Create, update, delete, or get Gateway objects from the Verity API.
- This module interacts with the `/gateways` endpoints.
module: gateways
options:
  data:
    description:
    - Gateway definition object.
    required: false
    suboptions:
      gateway:
        description:
        - Gateway definition object.
        required: true
        suboptions:
          name:
            description:
            - Gateway name.
            required: true
            suboptions:
              advertisement_interval:
                default: 30
                description:
                - 'The minimum time in seconds between sending route updates to BGP
                  neighbor '
                required: false
                type: int
              anycast_ip_mask:
                default: ''
                description:
                - The Anycast Address will be used to enable an IP routing redundancy
                  mechanism designed to allow for transparent failover across a leaf
                  pair at the first-hop IP router.
                required: false
                type: str
              bfd_detect_multiplier:
                default: 3
                description:
                - Configure the detection multiplier to determine packet loss
                required: false
                type: int
              bfd_multihop:
                default: false
                description:
                - Enable BFD Multi-Hop for Neighbor. This is used to detect failures
                  in the forwarding path between the BGP peers.
                required: false
                type: bool
              bfd_receive_interval:
                default: 300
                description:
                - Configure the minimum interval during which the system can receive
                  BFD control packets
                required: false
                type: int
              bfd_transmission_interval:
                default: 300
                description:
                - Configure the minimum transmission interval during which the system
                  can send BFD control packets
                required: false
                type: int
              connect_timer:
                default: 120
                description:
                - Time in seconds between sucessive attempts to Establish BGP session
                required: false
                type: int
              default_originate:
                default: false
                description:
                - Instructs BGP to generate and send a default route 0.0.0.0/0 to
                  the specified neighbor.
                required: false
                type: bool
              dynamic_bgp_limits:
                default: 0
                description:
                - Dynamic BGP Limits
                required: false
                type: int
              dynamic_bgp_subnet:
                default: ''
                description:
                - Dynamic BGP Subnet
                required: false
                type: str
              ebgp_multihop:
                default: 255
                description:
                - 'Allows external BGP neighbors to establish peering session multiple
                  network hops away. '
                required: false
                type: int
              egress_vlan:
                default: null
                description:
                - VLAN used to carry BGP TCP session
                required: false
                type: int
              enable:
                default: false
                description:
                - 'Enable object.

                  It''s highly recommended to set this value to true so that validation
                  on the object will be ran.'
                required: false
                type: bool
              enable_bfd:
                default: false
                description:
                - Enable BFD(Bi-Directional Forwarding)
                required: false
                type: bool
              export_route_map:
                default: ''
                description:
                - A route-map applied to routes exported into the current tenant from
                  the targeted BGP router with the purpose of filtering or modifying
                  the routes
                required: false
                type: str
              export_route_map_ref_type_:
                choices:
                - route_map
                default: null
                description:
                - Object type for export_route_map field
                required: false
                type: str
              fabric_interconnect:
                default: false
                description:
                - ''
                required: false
                type: bool
              gateway_mode:
                choices:
                - Dynamic BGP
                - Static BGP
                - Static
                - Default
                default: Static BGP
                description:
                - Gateway Mode. Can be BGP, Static, or Default
                required: false
                type: str
              helper_hop_ip_address:
                default: ''
                description:
                - Helper Hop IP Address
                required: false
                type: str
              hold_timer:
                default: 180
                description:
                - 'Time, in seconds,  used to determine failure of session Keepalive
                  messages received from remote BGP peer '
                required: false
                type: int
              import_route_map:
                default: ''
                description:
                - A route-map applied to routes imported into the current tenant from
                  the targeted BGP router with the purpose of filtering or modifying
                  the routes
                required: false
                type: str
              import_route_map_ref_type_:
                choices:
                - route_map
                default: null
                description:
                - Object type for import_route_map field
                required: false
                type: str
              keepalive_timer:
                default: 60
                description:
                - Interval in seconds between Keepalive messages sent to remote BGP
                  peer
                required: false
                type: int
              local_as_no_prepend:
                default: false
                description:
                - Do not prepend the local-as number to the AS-PATH for routes advertised
                  through this BGP gateway. The Local AS Number must be set for this
                  to be able to be set.
                required: false
                type: bool
              local_as_number:
                default: null
                description:
                - Local AS Number
                required: false
                type: int
              max_local_as_occurrences:
                default: 0
                description:
                - Allow routes with the local AS number in the AS-path, specifying
                  the maximum occurrences permitted before declaring a routing loop.
                  Leave blank or '0' to disable.
                required: false
                type: int
              md5_password:
                default: ''
                description:
                - MD5 password
                required: false
                type: str
              name:
                default: ''
                description:
                - Object Name. Must be unique.
                required: false
                type: str
              neighbor_as_number:
                default: null
                description:
                - 'Autonomous System Number of remote BGP peer '
                required: false
                type: int
              neighbor_ip_address:
                default: ''
                description:
                - IP address of remote BGP peer
                required: false
                type: str
              next_hop_self:
                default: false
                description:
                - Optional attribute that disables the normal BGP calculation of next-hops
                  for advertised routes and instead sets the next-hops for advertised
                  routes to the IP address of the switch itself.
                required: false
                type: bool
              object_properties:
                suboptions:
                  group:
                    default: ''
                    description:
                    - Group
                    required: false
                    type: str
                type: dict
              replace_as:
                default: false
                description:
                - Prepend only Local AS in updates to EBGP peers.
                required: false
                type: bool
              source_ip_address:
                default: ''
                description:
                - Source IP address used to override the default source address calculation
                  for BGP TCP session
                required: false
                type: str
              static_routes:
                elements: dict
                suboptions:
                  ad_value:
                    default: null
                    description:
                    - Administrative distancing value, also known as route preference
                      - values from 0-255
                    required: false
                    type: int
                  enable:
                    default: false
                    description:
                    - Enable of this static route
                    required: false
                    type: bool
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                  ipv4_route_prefix:
                    default: ''
                    description:
                    - IPv4 unicast IP address followed by a subnet mask length
                    required: false
                    type: str
                  next_hop_ip_address:
                    default: ''
                    description:
                    - Next Hop IP Address. Must be a unicast IP address
                    required: false
                    type: str
                type: list
              tenant:
                default: ''
                description:
                - Tenant
                required: false
                type: str
              tenant_ref_type_:
                choices:
                - tenant
                - site
                default: null
                description:
                - Object type for tenant field
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
short_description: Manage Gateways via Verity API
'''

EXAMPLES = r'''- name: Create Gateway
  verity.api.gateways:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      gateway:
        TestGateway:
          advertisement_interval: 1
          anycast_ip_mask: anycast_ip_mask
          bfd_detect_multiplier: 1
          bfd_multihop: true
          bfd_receive_interval: 1
          bfd_transmission_interval: 1
          connect_timer: 1
          default_originate: true
          dynamic_bgp_limits: 1
          dynamic_bgp_subnet: dynamic_bgp_subnet
          ebgp_multihop: 1
          egress_vlan: 1
          enable: true
          enable_bfd: true
          export_route_map: export_route_map
          export_route_map_ref_type_: route_map
          fabric_interconnect: true
          gateway_mode: Dynamic BGP
          helper_hop_ip_address: helper_hop_ip_address
          hold_timer: 1
          import_route_map: import_route_map
          import_route_map_ref_type_: route_map
          keepalive_timer: 1
          local_as_no_prepend: true
          local_as_number: 1
          max_local_as_occurrences: 1
          md5_password: md5_password
          name: name
          neighbor_as_number: 1
          neighbor_ip_address: neighbor_ip_address
          next_hop_self: true
          object_properties:
            group: group
          replace_as: true
          source_ip_address: source_ip_address
          static_routes:
          - ad_value: 1
            enable: true
            index: 1
            ipv4_route_prefix: ipv4_route_prefix
            next_hop_ip_address: next_hop_ip_address
          tenant: tenant
          tenant_ref_type_: tenant
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Gateway
  verity.api.gateways:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      gateway:
        TestGateway:
          advertisement_interval: 1
          anycast_ip_mask: anycast_ip_mask
          bfd_detect_multiplier: 1
          bfd_multihop: true
          bfd_receive_interval: 1
          bfd_transmission_interval: 1
          connect_timer: 1
          default_originate: true
          dynamic_bgp_limits: 1
          dynamic_bgp_subnet: dynamic_bgp_subnet
          ebgp_multihop: 1
          egress_vlan: 1
          enable: true
          enable_bfd: true
          export_route_map: export_route_map
          export_route_map_ref_type_: route_map
          fabric_interconnect: true
          gateway_mode: Dynamic BGP
          helper_hop_ip_address: helper_hop_ip_address
          hold_timer: 1
          import_route_map: import_route_map
          import_route_map_ref_type_: route_map
          keepalive_timer: 1
          local_as_no_prepend: true
          local_as_number: 1
          max_local_as_occurrences: 1
          md5_password: md5_password
          name: name
          neighbor_as_number: 1
          neighbor_ip_address: neighbor_ip_address
          next_hop_self: true
          object_properties:
            group: group
          replace_as: true
          source_ip_address: source_ip_address
          static_routes:
          - ad_value: 1
            enable: true
            index: 1
            ipv4_route_prefix: ipv4_route_prefix
            next_hop_ip_address: next_hop_ip_address
          tenant: tenant
          tenant_ref_type_: tenant
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Gateway
  verity.api.gateways:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      gateway_name: TestGateway
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Gateway object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "gateways", "/gateways")


def main():
    run_module()


if __name__ == '__main__':
    main()
