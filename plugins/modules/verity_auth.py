from ansible.module_utils.basic import AnsibleModule
from ansible_collections.be_networks.verity.plugins.module_utils.verity_api import authenticate


DOCUMENTATION = r'''author:
- BeyondEdge Networks (@yourhandle)
description:
- Authenticate with the Verity API.
- This module interacts with the `/auth` endpoints.
module: verity_auth
options:
  base_url:
    description:
    - vNetC base URL.
    required: true
    type: str
  password:
    description:
    - Password.
    required: true
    type: str
  username:
    description:
    - Username.
    required: true
    type: str
short_description: Authenticate with the Verity API
'''

EXAMPLES = r'''- name: Authenticate once
  be_networks.verity.verity_auth:
    base_url: "https://vnc-address.com"
    username: "admin"
    password: "******"
  register: auth_result
'''

RETURN = r'''
response:
  description: API response with details about the authentication.
  returned: always
  type: dict
'''


def main():
    module_args = dict(
        base_url=dict(type="str", required=True),
        username=dict(type="str", required=True, no_log=True),
        password=dict(type="str", required=True, no_log=True),
    )
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    token = authenticate(module, module.params["base_url"],
                         module.params["username"], module.params["password"])
    module.exit_json(changed=False, token=token, base_url=module.params["base_url"])


if __name__ == "__main__":
    main()
