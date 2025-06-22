from pydantic import Field, BaseModel
import httpx
from fastmcp import FastMCP

mcp = FastMCP("MCP Server Demo 🐨",
              instructions="MCP server that provides user information and login",)


# schemas for the tools

class GetUserParams(BaseModel): 
    """Input parameters to call the GET user API""" 
    user_id: int = Field(..., description="User ID to fetch")

class GetUserResult(BaseModel):
    """Result parameters from the response to GET user API."""
    id: int = Field(..., description="ID of the user")
    firstName: str = Field(..., description="First name of the user")
    lastName: str = Field(..., description="Last name of the user")
    email: str = Field(..., description="Email address of the user")
    username: str = Field(..., description="Username of the user")


class LoginParams(BaseModel):
    """Input parameters to call the POST /auth/login API."""
    username: str = Field(..., description="Username to authenticate and log in")
    password: str = Field(..., description="Password of the user to log in")

class LoginResult(BaseModel):
    """Result paramters from the response to the POST /auth/login API."""
    token: str = Field(..., description="Authentication token of the authenticated user.")

# tool implementations
@mcp.tool
async def get_user(user: GetUserParams) -> GetUserResult:
    """Gets the details of a user based on the user's id."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(url=f"https://dummyjson.com/users/{user.user_id}")
        resp.raise_for_status()
        data = resp.json()
        return GetUserResult(
            id=data["id"],
            firstName=data["firstName"],
            lastName=data["lastName"],
            email=data["email"],
            username=data["username"]
        )



