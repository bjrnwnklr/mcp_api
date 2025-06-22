import asyncio
from fastmcp import Client
from server import GetUserParams

client = Client("server.py")

async def call_tool(id: int):
    async with client:
        result = await client.call_tool("get_user", GetUserParams(user_id=id))
        print(result)

asyncio.run(call_tool(1))