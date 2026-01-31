from fastapi import FastAPI
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import uvicorn

def homepage(request):
    return JSONResponse({"status": "ok", "message": "HA MCP running"})

app = Starlette(
    debug=False,
    routes=[
        Route("/", homepage),
    ],
)

if __name__ == "__main__":
    import asyncio
    from starlette.servers import Server
    from starlette.config import Config

    config = Config(
        "ha_mcp_server:app",
        host="0.0.0.0",
        port=8000,
        loop="asyncio",
    )

    server = Server(config)
    asyncio.run(server.serve())
