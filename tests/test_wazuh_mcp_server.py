import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from wazuh_mcp_server import transform_to_mcp, WazuhAPIClient

def test_transform_to_mcp():
    event = {
        "id": "test-event",
        "category": "intrusion_detection",
        "severity": "high",
        "description": "Test description",
        "data": {"key": "value"}
    }
    mcp_message = transform_to_mcp(event, event_type="alert")
    assert mcp_message["protocol_version"] == "1.0"
    assert mcp_message["source"] == "Wazuh"
    assert mcp_message["context"]["id"] == "test-event"


def test_wazuh_api_client_base_url():
    client = WazuhAPIClient(
        host="example.com",
        port=55000,
        username="user",
        password="pass",
        verify_ssl=False,
        protocol="http",
    )
    assert client.base_url == "http://example.com:55000"
