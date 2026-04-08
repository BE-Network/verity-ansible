#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2026, BE Networks
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r'''author:
- BE Networks (@be_networks)
description:
- This module exists to provide documentation for the C(sample_action) action plugin.
module: sample_action
options:
  msg:
    description:
    - Message to display.
    required: false
    type: str
  prefix:
    description:
    - Optional prefix to prepend to C(msg).
    required: false
    type: str
short_description: Sample module used for action plugin documentation matching
'''

EXAMPLES = r'''
- name: Example usage of sample_action
  be_networks.verity.sample_action:
    msg: Hello
    prefix: Demo
'''

RETURN = r'''
message:
  description: The composed message.
  returned: always
  type: str
'''


def main():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            msg=dict(type='str', required=False),
            prefix=dict(type='str', required=False),
        ),
        supports_check_mode=True,
    )

    msg = module.params.get('msg') or ''
    prefix = module.params.get('prefix') or ''
    message = f"{prefix}: {msg}" if prefix else msg

    module.exit_json(changed=False, message=message)


if __name__ == '__main__':
    main()
