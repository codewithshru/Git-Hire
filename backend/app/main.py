"""GitHire API entrypoint.

Mounts module routers under /api/v1 and exposes health endpoints for
load-balancer probes. Feature routers are added as modules are implemented;
the app runs correctly with zero feature modules registered.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title="GitHire API",
        version="0.1.0",
        description="AI-powered hiring and career platform API",
        openapi_url="/api/v1/openapi.json",
        docs_url="/api/v1/docs",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health", tags=["health"])
    async def health() -> dict[str, str]:
        """Liveness probe."""
        return {"status": "ok"}

    @app.get("/health/ready", tags=["health"])
    async def readiness() -> dict[str, str]:
        """Readiness probe (DB/Redis checks arrive with core infrastructure)."""
        return {"status": "ok"}

    # Module routers are mounted here as features are implemented, e.g.:
    # app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])

    return app


app = create_app()
