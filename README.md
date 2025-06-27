# Wazuh MCP Server

A production-grade, open-source MCP server for integrating Wazuh security data with local LLM clients (e.g. Claude Desktop or AnythingLLM). This service authenticates with the Wazuh RESTful API, retrieves alerts from OpenSearch indices, transforms events into an MCP-compliant JSON format, and exposes an HTTP endpoint that LLM applications can query for real-time security context.

## Features

- **JWT-Based Authentication:** Securely authenticate with Wazuh using JWT tokens.
- **Alert Retrieval:** Query OpenSearch indices for Wazuh alert data.
- **MCP Message Transformation:** Convert security events into standardized MCP messages.
- **Flask HTTP Server: Exposes an `/mcp` endpoint for desktop LLM integration.
- **Robust Error Handling:** Handles token expiration, network timeouts, and malformed data.
- **Configurable:** Easily configure via environment variables and integrate with your desktop LLM client via its config file.


## Prerequisites

- Python 3.8+
- Access to a Wazuh API instance.
- (Optional) Claude Desktop configured to call the MCP server.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/unmuktoai/Wazuh-MCP-Server.git
   cd Wazuh-MCP-Server
Create and Activate a Virtual Environment:

  ```bash
  
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
**Install Dependencies:**

  ```bash
pip install -r requirements.txt
```
**Configuration**
Create a `.env` file in the project root with the following variables:

```bash
WAZUH_HOST=127.0.0.1
WAZUH_PORT=80
WAZUH_USER=user
WAZUH_PASS=pass
VERIFY_SSL=false
MCP_SERVER_PORT=8000
```

These values are examples; replace them with your real Wazuh credentials. The
server loads this file automatically on startup, so environment variables do not
need to be exported manually.
The repository includes a sample `.env` file populated with the above values for
reference. Do **not** commit production secrets to version control.
**Running the Server**
Start the MCP server with:

  ```bash
python wazuh_mcp_server.py 
```
The server will listen on all interfaces at the port specified by 
  ```bash
MCP_SERVER_PORT.
```
**Integration with Claude Desktop**
To integrate with Claude Desktop, update its configuration file:

MacOS: ~/Library/Application Support/Claude/claude_desktop_config.json
Windows: %APPDATA%/Claude/claude_desktop_config.json
Add the following entry under mcpServers:

  ```bash
{
  "mcpServers": {
    "mcp-server-wazuh": {
      "command": "python3 /path/to/Wazuh-MCP-Server/wazuh_mcp_server.py",
      "env": {
        "WAZUH_HOST": "your_wazuh_server",
        "WAZUH_PORT": "55000",
        "WAZUH_USER": "your_username",
        "WAZUH_PASS": "your_password",
        "WAZUH_PROTOCOL": "https",
        "MCP_SERVER_PORT": "8000",
        "VERIFY_SSL": "false"
      }
    }
  }
}
```
**Integration with AnythingLLM**
To use the MCP server with AnythingLLM, add a custom skill that issues HTTP requests to `http://<server>:<port>/mcp` and forwards the JSON response to the LLM.
License
This project is licensed under the MIT License.

Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

