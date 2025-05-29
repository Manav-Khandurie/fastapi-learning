from fastapi import FastAPI

from src.api.v1.api_router import api_router as router
from src.database.base import Base
from src.database.database import engine
from src.database.dependency import get_db
from src.graphql.router import router as graphql_router
from src.utils.helper import run_server
from src.utils.logger import logger
from src.utils.prometheus_instrumentation import setup_prometheus_instrumentation
from src.utils.tracing import setup_tracer

logger.info("Starting up the FastAPI application")
app = FastAPI()
Base.metadata.create_all(bind=engine)

# -----------------------HELPER--------------------
get_db()

# -----------------------PROMETHEUS--------------------
setup_prometheus_instrumentation(app)

# -----------------------JAEGER--------------------
setup_tracer(app)

# -----------------------ROUTER--------------------
app.include_router(router, prefix="/api/v1")
app.include_router(graphql_router, prefix="/graphql")
# -----------------------SERVER--------------------

if __name__ == "__main__":
    logger.info("Running server with `__main__`")
    run_server()
