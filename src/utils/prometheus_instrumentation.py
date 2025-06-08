from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from src.utils.logger import logger


def setup_prometheus_instrumentation(app: FastAPI):
    """
    Set up Prometheus instrumentation for the given FastAPI application.

    This function instruments the provided FastAPI app to expose Prometheus metrics
    at the /metrics endpoint. It logs the success or failure of the setup process.

    Args:
        app (FastAPI): The FastAPI application to instrument.
    """
    logger.info("🔧 Setting up Prometheus instrumentation")
    try:
        Instrumentator().instrument(app).expose(app)  # Instrument the app and expose metrics
        logger.success("✅ Prometheus metrics exposed at /metrics")
    except Exception as e:
        logger.exception(f"❌ Failed to set up Prometheus instrumentation: {e}")