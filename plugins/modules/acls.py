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
- Create, update, delete, or get ACL objects from the Verity API.
- This module interacts with the `/acls` endpoints.
module: acls
options:
  data:
    description:
    - ACL definition object.
    required: false
    suboptions:
      ip_filter:
        description:
        - ACL definition object.
        required: true
        suboptions:
          name:
            description:
            - ACL name.
            required: true
            suboptions:
              bidirectional:
                default: false
                description:
                - If bidirectional is selected, packets will be selected that match
                  the source filters in either the source or destination fields of
                  the packet.
                required: false
                type: bool
              destination_ip:
                default: ''
                description:
                - This field matches the destination IP address of an IPv4 packet.
                required: false
                type: str
              destination_port_1:
                default: null
                description:
                - This field is used for equal, greater-than or less-than TCP/UDP
                  port value in match operation. This field is also used for the lower
                  value in the range port match operation.
                required: false
                type: int
              destination_port_2:
                default: null
                description:
                - This field will only be used in the range TCP/UDP port value match
                  operation to define the top value in the range.
                required: false
                type: int
              destination_port_operator:
                choices:
                - ''
                - equal
                - greater
                - less
                - range
                default: ''
                description:
                - This field determines which match operation will be applied to TCP/UDP
                  ports. The choices are equal, greater, less or range.
                required: false
                type: str
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
                  notes:
                    default: ''
                    description:
                    - User Notes.
                    required: false
                    type: str
                type: dict
              protocol:
                default: ''
                description:
                - Value must be ip/tcp/udp/icmp or a number between 0 and 255 to match
                  packets.  Value IP will match all IP protocols.
                required: false
                type: str
              source_ip:
                default: ''
                description:
                - This field matches the source IP address of an IPv4 packet
                required: false
                type: str
              source_port_1:
                default: null
                description:
                - This field is used for equal, greater-than or less-than TCP/UDP
                  port value in match operation. This field is also used for the lower
                  value in the range port match operation.
                required: false
                type: int
              source_port_2:
                default: null
                description:
                - This field will only be used in the range TCP/UDP port value match
                  operation to define the top value in the range.
                required: false
                type: int
              source_port_operator:
                choices:
                - ''
                - equal
                - greater
                - less
                - range
                default: ''
                description:
                - This field determines which match operation will be applied to TCP/UDP
                  ports. The choices are equal, greater, less or range.
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
      ip_version:
        description:
        - No description provided
        required: true
        type: str
    type: dict
short_description: Manage ACLs via Verity API
'''

EXAMPLES = r'''- name: Create ACL
  be_networks.verity.acls:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      ip_filter:
        TestACL:
          bidirectional: true
          destination_ip: destination_ip
          destination_port_1: 1
          destination_port_2: 1
          destination_port_operator: ''
          enable: true
          name: name
          object_properties:
            notes: notes
          protocol: protocol
          source_ip: source_ip
          source_port_1: 1
          source_port_2: 1
          source_port_operator: ''
    params:
      changeset_name: changeset_name
      ip_version: ip_version
    token: '{{ auth_result.token }}'
- name: Edit ACL
  be_networks.verity.acls:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      ip_filter:
        TestACL:
          bidirectional: true
          destination_ip: destination_ip
          destination_port_1: 1
          destination_port_2: 1
          destination_port_operator: ''
          enable: true
          name: name
          object_properties:
            notes: notes
          protocol: protocol
          source_ip: source_ip
          source_port_1: 1
          source_port_2: 1
          source_port_operator: ''
    params:
      changeset_name: changeset_name
      ip_version: ip_version
    token: '{{ auth_result.token }}'
- name: Delete ACL
  be_networks.verity.acls:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      ip_filter_name: TestACL
      ip_version: ip_version
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the ACL object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "acls", "/acls")


def main():
    run_module()


if __name__ == '__main__':
    main()
