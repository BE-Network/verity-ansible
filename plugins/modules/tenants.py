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
- Create, update, delete, or get Tenant objects from the Verity API.
- This module interacts with the `/tenants` endpoints.
module: tenants
options:
  data:
    description:
    - Tenant definition object.
    required: false
    suboptions:
      tenant:
        description:
        - Tenant definition object.
        required: true
        suboptions:
          name:
            description:
            - Tenant name.
            required: true
            suboptions:
              default_originate:
                default: false
                description:
                - Enables a leaf switch to originate IPv4 default type-5 EVPN routes
                  across the switching fabric.
                required: false
                type: bool
              dhcp_relay_source_ipv4s_subnet:
                default: ''
                description:
                - Range of IPv4 addresses (represented in IPv4 subnet format) used
                  to configure the source IP of each DHCP Relay on each switch that
                  this Tenant is provisioned on.
                required: false
                type: str
              dhcp_relay_source_ipv6s_subnet:
                default: ''
                description:
                - Range of IPv6 addresses (represented in IPv6 subnet format) used
                  to configure the source IP of each DHCP Relay on each switch that
                  this Tenant is provisioned on.
                required: false
                type: str
              enable:
                default: true
                description:
                - 'Enable object.

                  It''s highly recommended to set this value to true so that validation
                  on the object will be ran.'
                required: false
                type: bool
              export_route_map:
                default: ''
                description:
                - A route-map applied to routes exported into the current tenant from
                  other tenants with the purpose of filtering or modifying the routes
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
              import_route_map:
                default: ''
                description:
                - A route-map applied to routes imported into the current tenant from
                  other tenants with the purpose of filtering or modifying the routes
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
              layer_3_vlan:
                default: null
                description:
                - 'VLAN value used to transport traffic between services of a Tenant '
                required: false
                type: int
              layer_3_vlan_auto_assigned_:
                default: null
                description:
                - Whether or not the value in layer_3_vlan field has been automatically
                  assigned or not. Set to false and change layer_3_vlan value to edit.
                required: false
                type: bool
              layer_3_vni:
                default: null
                description:
                - 'VNI value used to transport traffic between services of a Tenant '
                required: false
                type: int
              layer_3_vni_auto_assigned_:
                default: null
                description:
                - Whether or not the value in layer_3_vni field has been automatically
                  assigned or not. Set to false and change layer_3_vni value to edit.
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
                type: dict
              route_distinguisher:
                default: ''
                description:
                - Route Distinguishers are used to maintain uniqueness among identical
                  routes from different routers.  If set, then routes from this Tenant
                  will be identified with this Route Distinguisher (BGP Community).  It
                  should be two numbers separated by a colon.
                required: false
                type: str
              route_target_export:
                default: ''
                description:
                - 'A route-target (BGP Community) to attach while exporting routes
                  from the current tenant. It should be a comma-separated list of
                  BGP Communities: each Community being two numbers separated by a
                  colon.'
                required: false
                type: str
              route_target_import:
                default: ''
                description:
                - 'A route-target (BGP Community) to attach while importing routes
                  into the current tenant. It should be a comma-separated list of
                  BGP Communities: each Community being two numbers separated by a
                  colon.'
                required: false
                type: str
              route_tenants:
                elements: dict
                suboptions:
                  enable:
                    default: false
                    description:
                    - Enable
                    required: false
                    type: bool
                  index:
                    default: null
                    description:
                    - The index identifying the object. Zero if you want to add an
                      object to the list.
                    required: false
                    type: int
                  tenant:
                    default: ''
                    description:
                    - Tenant
                    required: false
                    type: str
                type: list
              vrf_name:
                default: (auto)
                description:
                - 'Virtual Routing and Forwarding instance name associated to tenants '
                required: false
                type: str
              vrf_name_auto_assigned_:
                default: null
                description:
                - Whether or not the value in vrf_name field has been automatically
                  assigned or not. Set to false and change vrf_name value to edit.
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
short_description: Manage Tenants via Verity API
'''

EXAMPLES = r'''- name: Create Tenant
  verity.api.tenants:
    action: create
    base_url: '{{ auth_result.base_url }}'
    data:
      tenant:
        TestTenant:
          default_originate: true
          dhcp_relay_source_ipv4s_subnet: dhcp_relay_source_ipv4s_subnet
          dhcp_relay_source_ipv6s_subnet: dhcp_relay_source_ipv6s_subnet
          enable: true
          export_route_map: export_route_map
          export_route_map_ref_type_: route_map
          import_route_map: import_route_map
          import_route_map_ref_type_: route_map
          layer_3_vlan: 1
          layer_3_vlan_auto_assigned_: true
          layer_3_vni: 1
          layer_3_vni_auto_assigned_: true
          name: name
          object_properties:
            group: group
          route_distinguisher: route_distinguisher
          route_target_export: route_target_export
          route_target_import: route_target_import
          route_tenants:
          - enable: true
            index: 1
            tenant: tenant
          vrf_name: vrf_name
          vrf_name_auto_assigned_: true
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Edit Tenant
  verity.api.tenants:
    action: update
    base_url: '{{ auth_result.base_url }}'
    data:
      tenant:
        TestTenant:
          default_originate: true
          dhcp_relay_source_ipv4s_subnet: dhcp_relay_source_ipv4s_subnet
          dhcp_relay_source_ipv6s_subnet: dhcp_relay_source_ipv6s_subnet
          enable: true
          export_route_map: export_route_map
          export_route_map_ref_type_: route_map
          import_route_map: import_route_map
          import_route_map_ref_type_: route_map
          layer_3_vlan: 1
          layer_3_vlan_auto_assigned_: true
          layer_3_vni: 1
          layer_3_vni_auto_assigned_: true
          name: name
          object_properties:
            group: group
          route_distinguisher: route_distinguisher
          route_target_export: route_target_export
          route_target_import: route_target_import
          route_tenants:
          - enable: true
            index: 1
            tenant: tenant
          vrf_name: vrf_name
          vrf_name_auto_assigned_: true
    params:
      changeset_name: changeset_name
    token: '{{ auth_result.token }}'
- name: Delete Tenant
  verity.api.tenants:
    action: delete
    base_url: '{{ auth_result.base_url }}'
    params:
      changeset_name: changeset_name
      tenant_name: TestTenant
    token: '{{ auth_result.token }}'
'''

RETURN = r'''
response:
  description: API response with details about the Tenant object.
  returned: always
  type: dict
'''


def run_module():
    module = AnsibleModule(argument_spec=MODULE_ARGS, supports_check_mode=True)
    run_resource(module, "tenants", "/tenants")


def main():
    run_module()


if __name__ == '__main__':
    main()
