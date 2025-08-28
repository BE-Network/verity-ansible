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
- Create, update, delete, or get Image Update Set objects from the Verity API.
- This module interacts with the `/imageupdatesets` endpoints.
module: imageupdatesets
options:
  data:
    description:
    - Image Update Set definition object.
    required: false
    suboptions:
      image_update_sets:
        description:
        - Image Update Set definition object.
        required: true
        suboptions:
          name:
            description:
            - Image Update Set name.
            required: true
            suboptions:
              comm_on_summary:
                default: true
                description:
                - Show Comm Pie Chart on Summary
                required: false
                type: bool
              enable:
                default: true
                description:
                - Enable object.
                required: false
                type: bool
              installation_on_summary:
                default: true
                description:
                - Show Installation Pie Chart on Summary
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
                  firmware_count:
                    default: 0
                    description:
                    - Firmware Count
                    required: false
                    type: int
                type: dict
              provisioning_on_summary:
                default: true
                description:
                - Show Provisioning Pie Chart on Summary
                required: false
                type: bool
              section:
                elements: dict
                suboptions:
                  endpoint_set_num_name:
                    default: ''
                    description:
                    - The name of the Endpoint Set
                    required: false
                    type: str
                  endpoint_set_num_on_summary:
                    default: true
                    description:
                    - Include on the Summary
                    required: false
                    type: bool
                  endpoint_set_num_subrule_1_inverted:
                    default: false
                    description:
                    - Subrule 1 Inverted of the Endpoint Set
                    required: false
                    type: bool
                  endpoint_set_num_subrule_1_reference_path:
                    default: ''
                    description:
                    - Subrule 1 Reference Path of the Endpoint Set
                    required: false
                    type: str
                  endpoint_set_num_subrule_1_reference_path_ref_type_:
                    default: null
                    description:
                    - Object type for endpoint_set_num_subrule_1_reference_path field
                    required: false
                    type: str
                  endpoint_set_num_subrule_1_type:
                    choices:
                    - ''
                    - productClass
                    - endpoint_type
                    - endpoint
                    - badge_color
                    - pod
                    - badge
                    - deviceSerialNumber
                    default: ''
                    description:
                    - Subrule 1 Type of the Endpoint Set
                    required: false
                    type: str
                  endpoint_set_num_subrule_1_value:
                    default: ''
                    description:
                    - Subrule 1 Value of the Endpoint Set
                    required: false
                    type: str
                  endpoint_set_num_subrule_2_inverted:
                    default: false
                    description:
                    - Subrule 2 Inverted of the Endpoint Set
                    required: false
                    type: bool
                  endpoint_set_num_subrule_2_reference_path:
                    default: ''
                    description:
                    - Subrule 2 Reference Path of the Endpoint Set
                    required: false
                    type: str
                  endpoint_set_num_subrule_2_reference_path_ref_type_:
                    default: null
                    description:
                    - Object type for endpoint_set_num_subrule_2_reference_path field
                    required: false
                    type: str
                  endpoint_set_num_subrule_2_type:
                    choices:
                    - ''
                    - productClass
                    - endpoint_type
                    - endpoint
                    - badge_color
                    - pod
                    - badge
                    - deviceSerialNumber
                    default: ''
                    description:
                    - Subrule 2 Type of the Endpoint Set
                    required: false
                    type: str
                  endpoint_set_num_subrule_2_value:
                    default: ''
                    description:
                    - Subrule 2 Value of the Endpoint Set
                    required: false
                    type: str
                  endpoint_set_num_subrule_3_inverted:
                    default: false
                    description:
                    - Subrule 3 Inverted of the Endpoint Set
                    required: false
                    type: bool
                  endpoint_set_num_subrule_3_reference_path:
                    default: ''
                    description:
                    - Subrule 3 Reference Path of the Endpoint Set
                    required: false
                    type: str
                  endpoint_set_num_subrule_3_reference_path_ref_type_:
                    default: null
                    description:
                    - Object type for endpoint_set_num_subrule_3_reference_path field
                    required: false
                    type: str
                  endpoint_set_num_subrule_3_type:
                    choices:
                    - ''
                    - productClass
                    - endpoint_type
                    - endpoint
                    - badge_color
                    - pod
                    - badge
                    - deviceSerialNumber
                    default: ''
                    description:
                    - Subrule 3 Type of the Endpoint Set
                    required: false
                    type: str
                  endpoint_set_num_subrule_3_value:
                    default: ''
                    description:
                    - Subrule 3 Value of the Endpoint Set
                    required: false
                    type: str
                  endpoint_set_num_target_upgrade_version:
                    choices:
                    - 1.8.1.5
                    - 1.8.1.4
                    - unmanaged
                    default: unmanaged
                    description:
                    - The target SW version for member devices of the Endpoint Set
                    required: false
                    type: str
                  endpoint_set_num_target_upgrade_version_time:
                    default: ''
                    description:
                    - The time to update to the target SW version
                    required: false
                    type: str
                  endpoint_set_num_unique_identifier:
                    default: '17553442285981'
                    description:
                    - Unique Identifier - not editable
                    required: false
                    type: str
                type: list
              section_else:
                elements: dict
                suboptions:
                  endpoint_set_for_all_others_target_upgrade_version:
                    choices:
                    - 1.8.1.5
                    - 1.8.1.4
                    - unmanaged
                    default: unmanaged
                    description:
                    - The target SW version for member devices of the Endpoint Set
                    required: false
                    type: str
                  endpoint_set_for_all_others_target_upgrade_version_time:
                    default: ''
                    description:
                    - The time to update to the target SW version
                    required: false
                    type: str
                  endpoint_set_for_all_others_unique_identifier:
                    default: else
                    description:
                    - Unique Identifier - not editable
                    required: false
                    type: str
                  endpoint_set_num_name:
                    default: All Others
                    description:
                    - The name of the Endpoint Set
                    required: false
                    type: str
                  endpoint_set_num_on_summary:
                    default: true
                    description:
                    - Include on the Summary
                    required: false
                    type: bool
                type: list
              section_pointless:
                elements: dict
                suboptions:
                  endpoint_set_for_endpointless_target_upgrade_version:
                    choices:
                    - 1.8.1.5
                    - 1.8.1.4
                    - unmanaged
                    default: unmanaged
                    description:
                    - The target SW version for member devices of the Endpoint Set
                    required: false
                    type: str
                  endpoint_set_for_endpointless_target_upgrade_version_time:
                    default: ''
                    description:
                    - The time to update to the target SW version
                    required: false
                    type: str
                  endpoint_set_for_endpointless_unique_identifier:
                    default: pointless
                    description:
                    - Unique Identifier - not editable
                    required: false
                    type: str
                  endpoint_set_num_name:
                    default: Unassigned Devices
                    description:
                    - The name of the Endpoint Set
                    required: false
                    type: str
                  endpoint_set_num_on_summary:
                    default: true
                    description:
                    - Include on the Summary
                    required: false
                    type: bool
                type: list
              type:
                choices:
                - whitebox
                - blackbox
                default: blackbox
                description:
                - Type of Image Update Sets
                required: false
                type: str
              upgrader_on_summary:
                default: true
                description:
                - Show Upgrader Pie Chart on Summary
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
short_description: Manage Image Update Sets via Verity API
'''

EXAMPLES = r'''- name: Create Image Update Set
  be_networks.verity.imageupdatesets:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      image_update_sets:
        TestImage Update Set:
          comm_on_summary: true
          enable: true
          installation_on_summary: true
          name: name
          object_properties:
            firmware_count: 1
          provisioning_on_summary: true
          section:
          - endpoint_set_num_name: endpoint_set_num_name
            endpoint_set_num_on_summary: true
            endpoint_set_num_subrule_1_inverted: true
            endpoint_set_num_subrule_1_reference_path: endpoint_set_num_subrule_1_reference_path
            endpoint_set_num_subrule_1_reference_path_ref_type_: endpoint_set_num_subrule_1_reference_path_ref_type_
            endpoint_set_num_subrule_1_type: ''
            endpoint_set_num_subrule_1_value: endpoint_set_num_subrule_1_value
            endpoint_set_num_subrule_2_inverted: true
            endpoint_set_num_subrule_2_reference_path: endpoint_set_num_subrule_2_reference_path
            endpoint_set_num_subrule_2_reference_path_ref_type_: endpoint_set_num_subrule_2_reference_path_ref_type_
            endpoint_set_num_subrule_2_type: ''
            endpoint_set_num_subrule_2_value: endpoint_set_num_subrule_2_value
            endpoint_set_num_subrule_3_inverted: true
            endpoint_set_num_subrule_3_reference_path: endpoint_set_num_subrule_3_reference_path
            endpoint_set_num_subrule_3_reference_path_ref_type_: endpoint_set_num_subrule_3_reference_path_ref_type_
            endpoint_set_num_subrule_3_type: ''
            endpoint_set_num_subrule_3_value: endpoint_set_num_subrule_3_value
            endpoint_set_num_target_upgrade_version: 1.8.1.5
            endpoint_set_num_target_upgrade_version_time: endpoint_set_num_target_upgrade_version_time
            endpoint_set_num_unique_identifier: endpoint_set_num_unique_identifier
          section_else:
          - endpoint_set_for_all_others_target_upgrade_version: 1.8.1.5
            endpoint_set_for_all_others_target_upgrade_version_time: endpoint_set_for_all_others_target_upgrade_version_time
            endpoint_set_for_all_others_unique_identifier: endpoint_set_for_all_others_unique_identifier
            endpoint_set_num_name: endpoint_set_num_name
            endpoint_set_num_on_summary: true
          section_pointless:
          - endpoint_set_for_endpointless_target_upgrade_version: 1.8.1.5
            endpoint_set_for_endpointless_target_upgrade_version_time: endpoint_set_for_endpointless_target_upgrade_version_time
            endpoint_set_for_endpointless_unique_identifier: endpoint_set_for_endpointless_unique_identifier
            endpoint_set_num_name: endpoint_set_num_name
            endpoint_set_num_on_summary: true
          type: whitebox
          upgrader_on_summary: true
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Image Update Set
  be_networks.verity.imageupdatesets:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      image_update_sets:
        TestImage Update Set:
          comm_on_summary: true
          enable: true
          installation_on_summary: true
          name: name
          object_properties:
            firmware_count: 1
          provisioning_on_summary: true
          section:
          - endpoint_set_num_name: endpoint_set_num_name
            endpoint_set_num_on_summary: true
            endpoint_set_num_subrule_1_inverted: true
            endpoint_set_num_subrule_1_reference_path: endpoint_set_num_subrule_1_reference_path
            endpoint_set_num_subrule_1_reference_path_ref_type_: endpoint_set_num_subrule_1_reference_path_ref_type_
            endpoint_set_num_subrule_1_type: ''
            endpoint_set_num_subrule_1_value: endpoint_set_num_subrule_1_value
            endpoint_set_num_subrule_2_inverted: true
            endpoint_set_num_subrule_2_reference_path: endpoint_set_num_subrule_2_reference_path
            endpoint_set_num_subrule_2_reference_path_ref_type_: endpoint_set_num_subrule_2_reference_path_ref_type_
            endpoint_set_num_subrule_2_type: ''
            endpoint_set_num_subrule_2_value: endpoint_set_num_subrule_2_value
            endpoint_set_num_subrule_3_inverted: true
            endpoint_set_num_subrule_3_reference_path: endpoint_set_num_subrule_3_reference_path
            endpoint_set_num_subrule_3_reference_path_ref_type_: endpoint_set_num_subrule_3_reference_path_ref_type_
            endpoint_set_num_subrule_3_type: ''
            endpoint_set_num_subrule_3_value: endpoint_set_num_subrule_3_value
            endpoint_set_num_target_upgrade_version: 1.8.1.5
            endpoint_set_num_target_upgrade_version_time: endpoint_set_num_target_upgrade_version_time
            endpoint_set_num_unique_identifier: endpoint_set_num_unique_identifier
          section_else:
          - endpoint_set_for_all_others_target_upgrade_version: 1.8.1.5
            endpoint_set_for_all_others_target_upgrade_version_time: endpoint_set_for_all_others_target_upgrade_version_time
            endpoint_set_for_all_others_unique_identifier: endpoint_set_for_all_others_unique_identifier
            endpoint_set_num_name: endpoint_set_num_name
            endpoint_set_num_on_summary: true
          section_pointless:
          - endpoint_set_for_endpointless_target_upgrade_version: 1.8.1.5
            endpoint_set_for_endpointless_target_upgrade_version_time: endpoint_set_for_endpointless_target_upgrade_version_time
            endpoint_set_for_endpointless_unique_identifier: endpoint_set_for_endpointless_unique_identifier
            endpoint_set_num_name: endpoint_set_num_name
            endpoint_set_num_on_summary: true
          type: whitebox
          upgrader_on_summary: true
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Image Update Set
  be_networks.verity.imageupdatesets:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      image_update_sets_name: TestImage Update Set
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Image Update Set object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "imageupdatesets", "/imageupdatesets")


def main():
    run_module()


if __name__ == '__main__':
    main()
