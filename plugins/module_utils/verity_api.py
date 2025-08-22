# -*- coding: utf-8 -*-
# Common utilities for Verity API modules

from ansible.module_utils.urls import open_url
import json


def authenticate(module, base_url, username, password):
    """
    Authenticate against the Verity API and return a token string.
    """
    url = f"{base_url}/api/auth"
    headers = {"Content-Type": "application/json"}
    payload = {"auth": {"username": username, "password": password}}

    try:
        response = open_url(
            url,
            method="POST",
            headers=headers,
            data=json.dumps(payload),
            validate_certs=not module.params.get("validate_certs", True),
            timeout=30,
        )
        resp_data = json.loads(response.read())
        token = resp_data.get("token")
        if not token:
            module.fail_json(msg="Authentication succeeded but no token returned", response=resp_data)
        return token
    except Exception as e:
        module.fail_json(msg=f"Authentication failed: {str(e)}")


def build_headers(token):
    """
    Build standard headers for API calls.
    """
    return {"Cookie": f"ivn_api={token}", "Content-Type": "application/json"}
