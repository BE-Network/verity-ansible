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
- Create, update, delete, or get Site objects from the Verity API.
- This module interacts with the `/sites` endpoints.
module: sites
options:
  data:
    description:
    - Site definition object.
    required: false
    suboptions:
      site:
        description:
        - Site definition object.
        required: true
        suboptions:
          name:
            description:
            - Site name.
            required: true
            suboptions:
              aggressive_reporting:
                default: true
                description:
                - Fast Reporting of Switch Communications, Link Up/Down, and BGP Status
                required: false
                type: bool
              anycast_mac_address:
                default: (auto)
                description:
                - Site Level MAC Address for Anycast
                required: false
                type: str
              anycast_mac_address_auto_assigned_:
                default: null
                description:
                - Whether or not the value in anycast_mac_address field has been automatically
                  assigned or not. Set to false and change anycast_mac_address value
                  to edit.
                required: false
                type: bool
              bgp_hold_down_timer:
                default: 180
                description:
                - Spine BGP Hold Down Timer
                required: false
                type: int
              bgp_keepalive_timer:
                default: 60
                description:
                - Spine BGP Keepalive Timer
                required: false
                type: int
              crc_failure_threshold:
                default: 5
                description:
                - Threshold in Errors per second that when met will disable the links
                  as part of LAGs
                required: false
                type: int
              dscp_to_p_bit_map:
                default: '0000000011111111222222223333333344444444555555556666666677777777'
                description:
                - For any Service that is using DSCP to TC map packet prioritization.
                  A string of length 64 with a 0-7 in each position
                required: false
                type: str
              enable:
                default: true
                description:
                - Enable object.
                required: false
                type: bool
              evpn_mac_holdtime:
                default: 1080
                description:
                - MAC Holdtime
                required: false
                type: int
              evpn_multihoming_startup_delay:
                default: 300
                description:
                - Startup Delay
                required: false
                type: int
              force_spanning_tree_on_fabric_ports:
                default: false
                description:
                - Enable spanning tree on all fabric connections.  This overrides
                  the Eth Port Settings for Fabric ports
                required: false
                type: bool
              islands:
                elements: dict
                suboptions:
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                  toi_switchpoint:
                    default: ''
                    description:
                    - TOI Switchpoint
                    required: false
                    type: str
                  toi_switchpoint_ref_type_:
                    choices:
                    - switchpoint
                    default: null
                    description:
                    - Object type for toi_switchpoint field
                    required: false
                    type: str
                type: list
              leaf_bgp_advertisement_interval:
                default: 1
                description:
                - BGP Advertisement Interval for leafs. Use "0" for immediate updates
                required: false
                type: int
              leaf_bgp_connect_timer:
                default: 120
                description:
                - BGP Connect Timer
                required: false
                type: int
              leaf_bgp_hold_down_timer:
                default: 180
                description:
                - Leaf BGP Hold Down Timer
                required: false
                type: int
              leaf_bgp_keep_alive_timer:
                default: 60
                description:
                - Leaf BGP Keep Alive Timer
                required: false
                type: int
              link_state_timeout_value:
                default: 60
                description:
                - Link State Timeout Value
                required: false
                type: int
              mac_address_aging_time:
                default: 600
                description:
                - MAC Address Aging Time (between 1-100000)
                required: false
                type: int
              mlag_delay_restore_timer:
                default: 300
                description:
                - MLAG Delay Restore Timer
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
                  system_graphs:
                    elements: dict
                    suboptions:
                      graph_num_data:
                        default: ''
                        description:
                        - The graph data detailing this graph choice
                        required: false
                        type: str
                      index:
                        default: null
                        description:
                        - The index identifying the object. Zero if you want to add
                          an object to the list.
                        required: false
                        type: int
                    type: list
                type: dict
              pairs:
                elements: dict
                suboptions:
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                  is_whitebox_pair:
                    default: false
                    description:
                    - LAG Pair
                    required: false
                    type: bool
                  lag_group:
                    default: ''
                    description:
                    - LAG Group
                    required: false
                    type: str
                  lag_group_ref_type_:
                    choices:
                    - lag
                    default: null
                    description:
                    - Object type for lag_group field
                    required: false
                    type: str
                  name:
                    default: ''
                    description:
                    - Object Name. Must be unique.
                    required: false
                    type: str
                  switchpoint_1:
                    default: ''
                    description:
                    - Switchpoint
                    required: false
                    type: str
                  switchpoint_1_ref_type_:
                    choices:
                    - switchpoint
                    default: null
                    description:
                    - Object type for switchpoint_1 field
                    required: false
                    type: str
                  switchpoint_2:
                    default: ''
                    description:
                    - Switchpoint
                    required: false
                    type: str
                  switchpoint_2_ref_type_:
                    choices:
                    - switchpoint
                    default: null
                    description:
                    - Object type for switchpoint_2 field
                    required: false
                    type: str
                type: list
              read_only_mode:
                default: false
                description:
                - When Read Only Mode is checked, vNetC will perform all functions
                  except writing database updates to the target hardware
                required: false
                type: bool
              region_name:
                default: ''
                description:
                - Defines the logical boundary of the network. All switches in an
                  MSTP region must have the same configured region name
                required: false
                type: str
              revision:
                default: 0
                description:
                - A logical number that signifies a revision for the MSTP configuration.
                  All switches in an MSTP region must have the same revision number
                required: false
                type: int
              service_for_site:
                default: service|Management|
                description:
                - Service for Site
                required: false
                type: str
              service_for_site_ref_type_:
                choices:
                - service
                default: null
                description:
                - Object type for service_for_site field
                required: false
                type: str
              spanning_tree_type:
                choices:
                - ''
                - pvst
                - mstp
                - port
                default: pvst
                description:
                - Sets the spanning tree type for all Ports in this Site with Spanning
                  Tree enabled
                required: false
                type: str
              spine_bgp_advertisement_interval:
                default: 1
                description:
                - BGP Advertisement Interval for spines/superspines. Use "0" for immediate
                  updates
                required: false
                type: int
              spine_bgp_connect_timer:
                default: 120
                description:
                - BGP Connect Timer
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
short_description: Manage Sites via Verity API
'''

EXAMPLES = r'''- name: Create Site
  be_networks.verity.sites:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      site:
        TestSite:
          aggressive_reporting: true
          anycast_mac_address: anycast_mac_address
          anycast_mac_address_auto_assigned_: true
          bgp_hold_down_timer: 1
          bgp_keepalive_timer: 1
          crc_failure_threshold: 1
          dscp_to_p_bit_map: dscp_to_p_bit_map
          enable: true
          evpn_mac_holdtime: 1
          evpn_multihoming_startup_delay: 1
          force_spanning_tree_on_fabric_ports: true
          islands:
          - index: 1
            toi_switchpoint: toi_switchpoint
            toi_switchpoint_ref_type_: switchpoint
          leaf_bgp_advertisement_interval: 1
          leaf_bgp_connect_timer: 1
          leaf_bgp_hold_down_timer: 1
          leaf_bgp_keep_alive_timer: 1
          link_state_timeout_value: 1
          mac_address_aging_time: 1
          mlag_delay_restore_timer: 1
          name: name
          object_properties:
            system_graphs:
            - graph_num_data: graph_num_data
              index: 1
          pairs:
          - index: 1
            is_whitebox_pair: true
            lag_group: lag_group
            lag_group_ref_type_: lag
            name: name
            switchpoint_1: switchpoint_1
            switchpoint_1_ref_type_: switchpoint
            switchpoint_2: switchpoint_2
            switchpoint_2_ref_type_: switchpoint
          read_only_mode: true
          region_name: region_name
          revision: 1
          service_for_site: service_for_site
          service_for_site_ref_type_: service
          spanning_tree_type: ''
          spine_bgp_advertisement_interval: 1
          spine_bgp_connect_timer: 1
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Site
  be_networks.verity.sites:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      site:
        TestSite:
          aggressive_reporting: true
          anycast_mac_address: anycast_mac_address
          anycast_mac_address_auto_assigned_: true
          bgp_hold_down_timer: 1
          bgp_keepalive_timer: 1
          crc_failure_threshold: 1
          dscp_to_p_bit_map: dscp_to_p_bit_map
          enable: true
          evpn_mac_holdtime: 1
          evpn_multihoming_startup_delay: 1
          force_spanning_tree_on_fabric_ports: true
          islands:
          - index: 1
            toi_switchpoint: toi_switchpoint
            toi_switchpoint_ref_type_: switchpoint
          leaf_bgp_advertisement_interval: 1
          leaf_bgp_connect_timer: 1
          leaf_bgp_hold_down_timer: 1
          leaf_bgp_keep_alive_timer: 1
          link_state_timeout_value: 1
          mac_address_aging_time: 1
          mlag_delay_restore_timer: 1
          name: name
          object_properties:
            system_graphs:
            - graph_num_data: graph_num_data
              index: 1
          pairs:
          - index: 1
            is_whitebox_pair: true
            lag_group: lag_group
            lag_group_ref_type_: lag
            name: name
            switchpoint_1: switchpoint_1
            switchpoint_1_ref_type_: switchpoint
            switchpoint_2: switchpoint_2
            switchpoint_2_ref_type_: switchpoint
          read_only_mode: true
          region_name: region_name
          revision: 1
          service_for_site: service_for_site
          service_for_site_ref_type_: service
          spanning_tree_type: ''
          spine_bgp_advertisement_interval: 1
          spine_bgp_connect_timer: 1
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Site
  be_networks.verity.sites:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      site_name: TestSite
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Site object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "sites", "/sites")


def main():
    run_module()


if __name__ == '__main__':
    main()
