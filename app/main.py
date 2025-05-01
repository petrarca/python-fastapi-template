from typing import Dict

from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from app.routes.api import api_router


# Define response models for better documentation
class WelcomeResponse(BaseModel):
    message: str
    
    class Config:
        schema_extra = {
            "example": {
                "message": "Welcome to FastAPI Application"
            }
        }


class HealthResponse(BaseModel):
    status: str
    
    class Config:
        schema_extra = {
            "example": {
                "status": "healthy"
            }
        }


# Set up templates and static files
templates = Jinja2Templates(directory="app/templates")

# Configure FastAPI application with detailed OpenAPI documentation
app = FastAPI(
    title="FastAPI Application",
    description="""A minimal FastAPI application template.
    
    ## Features
    
    * **RESTful API**: Modern API design with FastAPI
    * **OpenAPI Documentation**: Automatic interactive API documentation
    * **Modular Structure**: Well-organized code structure for scalability
    * **Template Rendering**: Server-side rendering with Jinja2
    
    ## API Endpoints
    
    * `/`: Home page with links to documentation
    * `/health`: Health check endpoint
    * `/api/hello`: Hello world API endpoint
    """,
    version="0.1.0",
    openapi_tags=[
        {
            "name": "API",
            "description": "API endpoints for the application",
        },
        {
            "name": "System",
            "description": "System endpoints for monitoring and status",
        },
    ],
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# Mount static files directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Register the API router
app.include_router(api_router)


@app.get(
    "/",
    response_class=HTMLResponse,
    status_code=status.HTTP_200_OK,
    summary="Home Page",
    description="Renders the home page with links to documentation.",
    tags=["System"],
)
async def home(request: Request):
    """Home page endpoint rendering a template.
    
    This endpoint serves as the entry point to the application and renders
    a beautiful home page with links to documentation and API endpoints.
    
    Args:
        request: The incoming request object
        
    Returns:
        HTMLResponse: The rendered HTML template
    """
    return templates.TemplateResponse(
        "home.html",
        {"request": request}
    )


@app.get(
    "/health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Health Check",
    description="Returns the health status of the application.",
    tags=["System"],
)
async def health() -> Dict[str, str]:
    """Health check endpoint.
    
    This endpoint can be used for monitoring and health checks.
    
    Returns:
        Dict[str, str]: A dictionary with the health status
    """
    return {"status": "healthy"}
