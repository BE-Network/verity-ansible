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
- Create, update, delete, or get Switchpoint objects from the Verity API.
- This module interacts with the `/switchpoints` endpoints.
module: switchpoints
options:
  data:
    description:
    - Switchpoint definition object.
    required: false
    suboptions:
      switchpoint:
        description:
        - Switchpoint definition object.
        required: true
        suboptions:
          name:
            description:
            - Switchpoint name.
            required: true
            suboptions:
              badges:
                elements: dict
                suboptions:
                  badge:
                    default: ''
                    description:
                    - Enable of this POTS port
                    required: false
                    type: str
                  badge_ref_type_:
                    choices:
                    - badge
                    default: null
                    description:
                    - Object type for badge field
                    required: false
                    type: str
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                type: list
              bgp_as_number:
                default: null
                description:
                - 'BGP Autonomous System Number for the site underlay '
                required: false
                type: int
              bgp_as_number_auto_assigned_:
                default: null
                description:
                - Whether or not the value in bgp_as_number field has been automatically
                  assigned or not. Set to false and change bgp_as_number value to
                  edit.
                required: false
                type: bool
              children:
                elements: dict
                suboptions:
                  child_num_device:
                    default: ''
                    description:
                    - Device associated with the Child
                    required: false
                    type: str
                  child_num_endpoint:
                    default: ''
                    description:
                    - Switchpoint associated with the Child
                    required: false
                    type: str
                  child_num_endpoint_ref_type_:
                    choices:
                    - switchpoint
                    default: null
                    description:
                    - Object type for child_num_endpoint field
                    required: false
                    type: str
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                type: list
              connected_bundle:
                default: ''
                description:
                - Connected Bundle
                required: false
                type: str
              connected_bundle_ref_type_:
                choices:
                - endpoint_bundle
                default: null
                description:
                - Object type for connected_bundle field
                required: false
                type: str
              device_serial_number:
                default: ''
                description:
                - Device Serial Number
                required: false
                type: str
              disabled_ports:
                default: ''
                description:
                - 'Disabled Ports

                  It''s a comma separated list of ports to disable.'
                required: false
                type: str
              eths:
                elements: dict
                suboptions:
                  breakout:
                    choices:
                    - 8x1G
                    - 2x10G
                    - pg200G
                    - 1x50G
                    - pg100G
                    - 2x400G
                    - 8x400G
                    - 4x100G
                    - 1x40G
                    - 1x1G
                    - 2x25G
                    - pg1G
                    - 8x10G
                    - 2x40G
                    - 1x200G
                    - 2x50G
                    - 4x40G
                    - pg800G
                    - pg10G
                    - 4x50G
                    - 8x40G
                    - 8x200G
                    - 8x100G
                    - 8x50G
                    - pg40G
                    - ''
                    - 1x25G
                    - 2x800G
                    - 4x400G
                    - 1x10G
                    - 4x25G
                    - 4x1G
                    - 2x100G
                    - 8x800G
                    - 8x25G
                    - pg400G
                    - 1x800G
                    - 2x200G
                    - 4x200G
                    - pg25G
                    - 1x100G
                    - 2x1G
                    - 1x400G
                    - 4x10G
                    - 4x800G
                    - pg50G
                    default: ''
                    description:
                    - Breakout Port Override. Available options determined by Switch
                      capability, Installed SFP and the capacity of the pipeline.
                    required: false
                    type: str
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                type: list
              locked:
                default: false
                description:
                - Permission lock
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
                  aggregate:
                    default: false
                    description:
                    - For Switch Endpoints. Denotes switch aggregated with all of
                      its sub switches
                    required: false
                    type: bool
                  eths:
                    elements: dict
                    suboptions:
                      eth_num_icon:
                        default: empty
                        description:
                        - Icon of this Eth Port
                        required: false
                        type: str
                      eth_num_label:
                        default: ''
                        description:
                        - Label of this Eth Port
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
                  expected_parent_endpoint:
                    default: ''
                    description:
                    - Expected Parent Endpoint
                    required: false
                    type: str
                  expected_parent_endpoint_ref_type_:
                    choices:
                    - switchpoint
                    default: null
                    description:
                    - Object type for expected_parent_endpoint field
                    required: false
                    type: str
                  is_host:
                    default: false
                    description:
                    - For Switch Endpoints. Denotes the Host Switch
                    required: false
                    type: bool
                  number_of_multipoints:
                    default: 0
                    description:
                    - Number of Multipoints
                    required: false
                    type: int
                  user_notes:
                    default: ''
                    description:
                    - Notes writen by User about the site
                    required: false
                    type: str
                type: dict
              out_of_band_management:
                default: false
                description:
                - For Switch Endpoints. Denotes a Switch is managed out of band via
                  the management port
                required: false
                type: bool
              pod:
                default: ''
                description:
                - Pod - subgrouping of spine and leaf switches
                required: false
                type: str
              pod_ref_type_:
                choices:
                - pod
                default: null
                description:
                - Object type for pod field
                required: false
                type: str
              rack:
                default: ''
                description:
                - 'Physical Rack location of the Switch '
                required: false
                type: str
              read_only_mode:
                default: false
                description:
                - When Read Only Mode is checked, vNetC will perform all functions
                  except writing database updates to the target hardware
                required: false
                type: bool
              super_pod:
                default: ''
                description:
                - Super Pod  subgrouping of super spines and pods
                required: false
                type: str
              switch_router_id_ip_mask:
                default: (auto)
                description:
                - Switch BGP Router Identifier
                required: false
                type: str
              switch_router_id_ip_mask_auto_assigned_:
                default: null
                description:
                - Whether or not the value in switch_router_id_ip_mask field has been
                  automatically assigned or not. Set to false and change switch_router_id_ip_mask
                  value to edit.
                required: false
                type: bool
              switch_vtep_id_ip_mask:
                default: (auto)
                description:
                - Switch VETP Identifier
                required: false
                type: str
              switch_vtep_id_ip_mask_auto_assigned_:
                default: null
                description:
                - Whether or not the value in switch_vtep_id_ip_mask field has been
                  automatically assigned or not. Set to false and change switch_vtep_id_ip_mask
                  value to edit.
                required: false
                type: bool
              traffic_mirrors:
                elements: dict
                suboptions:
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                  traffic_mirror_num_destination_port:
                    default: ''
                    description:
                    - Destination Port for Traffic Mirror
                    required: false
                    type: str
                  traffic_mirror_num_enable:
                    default: false
                    description:
                    - Enable Traffic Mirror
                    required: false
                    type: bool
                  traffic_mirror_num_inbound_traffic:
                    default: false
                    description:
                    - Boolean value indicating if the mirror is for inbound traffic
                    required: false
                    type: bool
                  traffic_mirror_num_outbound_traffic:
                    default: false
                    description:
                    - Boolean value indicating if the mirror is for outbound traffic
                    required: false
                    type: bool
                  traffic_mirror_num_source_lag_indicator:
                    default: false
                    description:
                    - Source LAG Indicator for Traffic Mirror
                    required: false
                    type: bool
                  traffic_mirror_num_source_port:
                    default: ''
                    description:
                    - Source Port for Traffic Mirror
                    required: false
                    type: str
                type: list
              type:
                choices:
                - ''
                - packet_broker
                - management
                - leaf
                - spine
                - packet_broker_tor
                - superspine
                - enterprise
                default: leaf
                description:
                - Type of Switchpoint
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
short_description: Manage Switchpoints via Verity API
'''

EXAMPLES = r'''- name: Create Switchpoint
  verity.api.switchpoints:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      switchpoint:
        TestSwitchpoint:
          badges:
          - badge: badge
            badge_ref_type_: badge
            index: 1
          bgp_as_number: 1
          bgp_as_number_auto_assigned_: true
          children:
          - child_num_device: child_num_device
            child_num_endpoint: child_num_endpoint
            child_num_endpoint_ref_type_: switchpoint
            index: 1
          connected_bundle: connected_bundle
          connected_bundle_ref_type_: endpoint_bundle
          device_serial_number: device_serial_number
          disabled_ports: disabled_ports
          eths:
          - breakout: 8x1G
            index: 1
          locked: true
          name: name
          object_properties:
            aggregate: true
            eths:
            - eth_num_icon: eth_num_icon
              eth_num_label: eth_num_label
              index: 1
            expected_parent_endpoint: expected_parent_endpoint
            expected_parent_endpoint_ref_type_: switchpoint
            is_host: true
            number_of_multipoints: 1
            user_notes: user_notes
          out_of_band_management: true
          pod: pod
          pod_ref_type_: pod
          rack: rack
          read_only_mode: true
          super_pod: super_pod
          switch_router_id_ip_mask: switch_router_id_ip_mask
          switch_router_id_ip_mask_auto_assigned_: true
          switch_vtep_id_ip_mask: switch_vtep_id_ip_mask
          switch_vtep_id_ip_mask_auto_assigned_: true
          traffic_mirrors:
          - index: 1
            traffic_mirror_num_destination_port: traffic_mirror_num_destination_port
            traffic_mirror_num_enable: true
            traffic_mirror_num_inbound_traffic: true
            traffic_mirror_num_outbound_traffic: true
            traffic_mirror_num_source_lag_indicator: true
            traffic_mirror_num_source_port: traffic_mirror_num_source_port
          type: ''
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Switchpoint
  verity.api.switchpoints:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      switchpoint:
        TestSwitchpoint:
          badges:
          - badge: badge
            badge_ref_type_: badge
            index: 1
          bgp_as_number: 1
          bgp_as_number_auto_assigned_: true
          children:
          - child_num_device: child_num_device
            child_num_endpoint: child_num_endpoint
            child_num_endpoint_ref_type_: switchpoint
            index: 1
          connected_bundle: connected_bundle
          connected_bundle_ref_type_: endpoint_bundle
          device_serial_number: device_serial_number
          disabled_ports: disabled_ports
          eths:
          - breakout: 8x1G
            index: 1
          locked: true
          name: name
          object_properties:
            aggregate: true
            eths:
            - eth_num_icon: eth_num_icon
              eth_num_label: eth_num_label
              index: 1
            expected_parent_endpoint: expected_parent_endpoint
            expected_parent_endpoint_ref_type_: switchpoint
            is_host: true
            number_of_multipoints: 1
            user_notes: user_notes
          out_of_band_management: true
          pod: pod
          pod_ref_type_: pod
          rack: rack
          read_only_mode: true
          super_pod: super_pod
          switch_router_id_ip_mask: switch_router_id_ip_mask
          switch_router_id_ip_mask_auto_assigned_: true
          switch_vtep_id_ip_mask: switch_vtep_id_ip_mask
          switch_vtep_id_ip_mask_auto_assigned_: true
          traffic_mirrors:
          - index: 1
            traffic_mirror_num_destination_port: traffic_mirror_num_destination_port
            traffic_mirror_num_enable: true
            traffic_mirror_num_inbound_traffic: true
            traffic_mirror_num_outbound_traffic: true
            traffic_mirror_num_source_lag_indicator: true
            traffic_mirror_num_source_port: traffic_mirror_num_source_port
          type: ''
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Switchpoint
  verity.api.switchpoints:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      switchpoint_name: TestSwitchpoint
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Switchpoint object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "switchpoints", "/switchpoints")


def main():
    run_module()


if __name__ == '__main__':
    main()
