import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def call_tool(tool_name: str, args: dict):

    try:

        server_params = StdioServerParameters(
            command="python",
            args=["mcp_app/mcp_server.py"]
        )

        async with stdio_client(server_params) as (read, write):

            async with ClientSession(read, write) as session:

                await session.initialize()

                result = await session.call_tool(tool_name, args)

                return result.content

    except Exception as e:
        # 🔥 IMPORTANT: expose real MCP error
        return {
            "mcp_error": str(e)
        }