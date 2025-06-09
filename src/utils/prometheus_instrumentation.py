from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from src.utils.logger import logger


def setup_prometheus_instrumentation(app: FastAPI):
    """Set up Prometheus instrumentation for the given FastAPI application.

    Args:
        app (FastAPI): The FastAPI application to instrument with Prometheus.
    
    Logs the setup process and any exceptions that occur during instrumentation.
    """
    logger.info("🔧 Setting up Prometheus instrumentation")
    try:
        Instrumentator().instrument(app).expose(app)
        logger.success("✅ Prometheus metrics exposed at /metrics")
    except Exception as e:
        logger.exception(f"❌ Failed to set up Prometheus instrumentation: {e}")