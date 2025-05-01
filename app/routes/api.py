from typing import Dict

from fastapi import APIRouter, status
from pydantic import BaseModel

# Create API router with tags for grouping in documentation
api_router = APIRouter(prefix="/api", tags=["API"])


# Response model for hello endpoint
class HelloResponse(BaseModel):
    result: str
    
    class Config:
        schema_extra = {
            "example": {
                "result": "world"
            }
        }


@api_router.get(
    "/hello",
    response_model=HelloResponse,
    status_code=status.HTTP_200_OK,
    summary="Hello World Endpoint",
    description="Returns a simple 'world' response to demonstrate the API.",
    response_description="Successful response with 'world' as the result.",
)
async def hello() -> Dict[str, str]:
    """Hello endpoint that returns 'world'.
    
    This is a simple endpoint that demonstrates the API functionality.
    It always returns the string 'world' as the result.
    
    Returns:
        Dict[str, str]: A dictionary with a single key 'result' and value 'world'
    """
    return {"result": "world"}
