import click
import uvicorn


@click.command()
@click.option(
    "--host",
    default="0.0.0.0",
    help="Host to bind the server to",
    show_default=True,
)
@click.option(
    "--port",
    default=8080,
    type=int,
    help="Port to bind the server to",
    show_default=True,
)
@click.option(
    "--reload/--no-reload",
    default=True,
    help="Enable/disable automatic reloading on code changes",
    show_default=True,
)
def run(host: str, port: int, reload: bool):
    """Run the FastAPI application with the specified options."""
    click.echo(f"Starting server at {host}:{port} (reload={'enabled' if reload else 'disabled'})")
    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=reload,
    )


if __name__ == "__main__":
    run()
