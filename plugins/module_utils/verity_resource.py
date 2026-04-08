from ansible_collections.be_networks.verity.plugins.module_utils.verity_api import (
    authenticate,
    build_headers,
)
import json

from ansible.module_utils.urls import open_url

MODULE_ARGS = dict(
    base_url=dict(type="str", required=True),
    username=dict(type="str", required=False, no_log=True),
    password=dict(type="str", required=False, no_log=True),
    params=dict(type="dict", required=False, default=None),
    data=dict(type="dict", required=False),
    token=dict(type="str", required=False, no_log=True),
    action=dict(type="str", choices=["create", "update", "delete"], default="create"),
)


def run_resource(module, resource_name, path):
    """
    Generic resource runner for Verity API modules.
    - resource_name: "acls", "badges", etc.
    - path: relative API path, e.g. "/acls"
    - payload_key: optional wrapper key for payload
    """

    base_url = module.params["base_url"]
    token = module.params["token"]
    username = module.params["username"]
    password = module.params["password"]
    data = module.params.get("data")
    params = module.params.get("params")
    action = module.params["action"]

    if not token:
        # Fallback: authenticate with username/password
        if not username or not password:
            module.fail_json(msg="Either token or username/password must be provided")
        token = authenticate(module, base_url, username, password)
    headers = build_headers(token)

    url = f"{base_url}/api{path}"

    result = dict(changed=False, response={})

    try:
        if action in ['create', 'update']:
            method = "PUT" if module.params["action"] == "create" else "PATCH"
            response = open_url(
                url,
                method=method,
                headers=headers,
                data=json.dumps(data or {}),
                timeout=30,
            )
            result["changed"] = True
            try:
                result["response"] = json.loads(response.read())
            except Exception:
                result["response"] = response.read().decode("utf-8", errors="replace")
        elif action == "delete":
            response = open_url(
                url,
                method="DELETE",
                headers=headers,
                timeout=30,
            )
            result["changed"] = True
            try:
                result["response"] = json.loads(response.read())
            except Exception:
                result["response"] = response.read().decode("utf-8", errors="replace")
    except Exception as e:
        module.fail_json(msg=f"{resource_name} API call failed: {str(e)}")

    module.exit_json(**result)
