# Wazuh MCP Server

A lightweight MCP server for interacting with Wazuh via local LLM clients. The server uses [fastmcp](https://pypi.org/project/fastmcp/) and exposes commands that can be called from LM Studio or any MCP compatible client.

## Installation

```bash
git clone https://github.com/Karibusan/Wazuh-MCP-Server
cd Wazuh-MCP-Server
cp .env.example .env
pip install -r requirements.txt
python wazuh_mcp_server.py
```

Compatible LM Studio via MCP config :

```json
{
  "mcpServers": {
    "wazuh": {
      "command": "python C:\\Projects\\wazuh-MCP-Server\\wazuh_mcp_server.py"
    }
  }
}
```
