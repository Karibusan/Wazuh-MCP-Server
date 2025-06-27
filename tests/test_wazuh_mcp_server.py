import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import types
import pytest

import wazuh_mcp_server as server

class DummyResponse:
    def __init__(self, status_code, json_data=None):
        self.status_code = status_code
        self._json = json_data or {}

    def json(self):
        return self._json


def test_list_agents_success(monkeypatch):
    def post(url, json=None, auth=None, verify=None):
        return DummyResponse(200, {"data": {"token": "abc"}})

    def get(url, headers=None, verify=None):
        return DummyResponse(200, {"agents": []})

    monkeypatch.setattr(server.requests, "post", post)
    monkeypatch.setattr(server.requests, "get", get)

    resp = server.list_agents(types.SimpleNamespace())
    assert resp.data == {"agents": []}
    assert resp.error is None
