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
- Create, update, delete, or get Eth-Port Profile objects from the Verity API.
- This module interacts with the `/ethportprofiles` endpoints.
module: ethportprofiles
options:
  data:
    description:
    - Eth-Port Profile definition object.
    required: false
    suboptions:
      eth_port_profile_:
        description:
        - Eth-Port Profile definition object.
        required: true
        suboptions:
          name:
            description:
            - Eth-Port Profile name.
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
                  port_monitoring:
                    choices:
                    - critical
                    - high
                    - ''
                    default: high
                    description:
                    - Defines importance of Link Down on this port
                    required: false
                    type: str
                type: dict
              services:
                elements: dict
                suboptions:
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                  row_num_enable:
                    default: false
                    description:
                    - Enable row
                    required: false
                    type: bool
                  row_num_external_vlan:
                    default: null
                    description:
                    - 'Choose an external vlan

                      A value of 0 will make the VLAN untagged, while in case null
                      is provided, the VLAN will be the one associated with the service.'
                    required: false
                    type: int
                  row_num_service:
                    default: ''
                    description:
                    - Choose a Service to connect
                    required: false
                    type: str
                  row_num_service_ref_type_:
                    choices:
                    - service
                    default: null
                    description:
                    - Object type for row_num_service field
                    required: false
                    type: str
                type: list
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
short_description: Manage Eth-Port Profiles via Verity API
'''

EXAMPLES = r'''- name: Create Eth-Port Profile
  be_networks.verity.ethportprofiles:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      eth_port_profile_:
        TestEth-Port Profile:
          enable: true
          name: name
          object_properties:
            group: group
            port_monitoring: critical
          services:
          - index: 1
            row_num_enable: true
            row_num_external_vlan: 1
            row_num_service: row_num_service
            row_num_service_ref_type_: service
          tenant_slice_managed: true
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Eth-Port Profile
  be_networks.verity.ethportprofiles:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      eth_port_profile_:
        TestEth-Port Profile:
          enable: true
          name: name
          object_properties:
            group: group
            port_monitoring: critical
          services:
          - index: 1
            row_num_enable: true
            row_num_external_vlan: 1
            row_num_service: row_num_service
            row_num_service_ref_type_: service
          tenant_slice_managed: true
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Eth-Port Profile
  be_networks.verity.ethportprofiles:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      eth_port_profile__name: TestEth-Port Profile
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Eth-Port Profile object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "ethportprofiles", "/ethportprofiles")


def main():
    run_module()


if __name__ == '__main__':
    main()
