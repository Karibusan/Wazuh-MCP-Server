from fastmcp.server import MCPServer
from fastmcp.types import MCPRequest, MCPResponse
from dotenv import load_dotenv
import os
import requests

load_dotenv()

WAZUH_HOST = os.getenv("WAZUH_HOST")
WAZUH_PORT = os.getenv("WAZUH_PORT", "443")
WAZUH_USER = os.getenv("WAZUH_USER")
WAZUH_PASS = os.getenv("WAZUH_PASS")
WAZUH_PROTO = os.getenv("WAZUH_PROTOCOL", "https")
VERIFY_SSL = os.getenv("VERIFY_SSL", "false").lower() == "true"

BASE_URL = f"{WAZUH_PROTO}://{WAZUH_HOST}:{WAZUH_PORT}"


def list_agents(request: MCPRequest) -> MCPResponse:
    auth_url = f"{BASE_URL}/security/user/authenticate"
    auth_data = {"raw": True}
    auth_res = requests.post(
        auth_url,
        json=auth_data,
        auth=(WAZUH_USER, WAZUH_PASS),
        verify=VERIFY_SSL,
    )

    if auth_res.status_code != 200:
        return MCPResponse(error="Auth failed")

    token = auth_res.json().get("data", {}).get("token")
    headers = {"Authorization": f"Bearer {token}"}
    agent_url = f"{BASE_URL}/agents"
    res = requests.get(agent_url, headers=headers, verify=VERIFY_SSL)

    if res.status_code != 200:
        return MCPResponse(error="Error fetching agents")

    return MCPResponse(data=res.json())


server = MCPServer()
server.command("list_agents")(list_agents)

if __name__ == "__main__":
    server.run()
