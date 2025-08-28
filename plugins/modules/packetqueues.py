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
- Create, update, delete, or get Packet Queue objects from the Verity API.
- This module interacts with the `/packetqueues` endpoints.
module: packetqueues
options:
  data:
    description:
    - Packet Queue definition object.
    required: false
    suboptions:
      packet_queue:
        description:
        - Packet Queue definition object.
        required: true
        suboptions:
          name:
            description:
            - Packet Queue name.
            required: true
            suboptions:
              enable:
                default: false
                description:
                - Enable object.
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
                  isdefault:
                    default: false
                    description:
                    - Default object.
                    required: false
                    type: bool
                type: dict
              pbit:
                elements: dict
                suboptions:
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                  packet_queue_for_p_bit:
                    default: 0
                    description:
                    - Flag indicating this Traffic Class' Queue
                    required: false
                    type: int
                type: list
              queue:
                elements: dict
                suboptions:
                  bandwidth_for_queue:
                    default: 0
                    description:
                    - Percentage bandwidth allocated to Queue. 0 is no limit
                    required: false
                    type: int
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                  scheduler_type:
                    choices:
                    - ''
                    - WRR
                    - SP
                    - DWRR
                    default: SP
                    description:
                    - Scheduler Type for Queue
                    required: false
                    type: str
                  scheduler_weight:
                    default: 0
                    description:
                    - Weight associated with WRR or DWRR scheduler
                    required: false
                    type: int
                type: list
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
short_description: Manage Packet Queues via Verity API
'''

EXAMPLES = r'''- name: Create Packet Queue
  be_networks.verity.packetqueues:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      packet_queue:
        TestPacket Queue:
          enable: true
          name: name
          object_properties:
            group: group
            isdefault: true
          pbit:
          - index: 1
            packet_queue_for_p_bit: 1
          queue:
          - bandwidth_for_queue: 1
            index: 1
            scheduler_type: ''
            scheduler_weight: 1
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Packet Queue
  be_networks.verity.packetqueues:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      packet_queue:
        TestPacket Queue:
          enable: true
          name: name
          object_properties:
            group: group
            isdefault: true
          pbit:
          - index: 1
            packet_queue_for_p_bit: 1
          queue:
          - bandwidth_for_queue: 1
            index: 1
            scheduler_type: ''
            scheduler_weight: 1
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Packet Queue
  be_networks.verity.packetqueues:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      packet_queue_name: TestPacket Queue
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Packet Queue object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "packetqueues", "/packetqueues")


def main():
    run_module()


if __name__ == '__main__':
    main()
