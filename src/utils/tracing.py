# src/utils/tracing.py
from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter as OTLPSpanExporterGRPC,
)
from opentelemetry.exporter.otlp.proto.http.trace_exporter import (
    OTLPSpanExporter as OTLPSpanExporterHTTP,
)
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from src.config.config import settings
from src.utils.logger import logger


def setup_tracer(app: FastAPI, log_correlation: bool = True) -> None:
    """
    Set up the OpenTelemetry tracer for the FastAPI application.

    Args:
        app (FastAPI): The FastAPI application instance.
        log_correlation (bool): Flag to enable logging correlation. Defaults to True.
    """
    MODE = settings.JAEGER_MODE
    OTLP_GRPC_ENDPOINT = settings.JAEGER_OTLP_GRPC_ENDPOINT
    OTLP_HTTP_ENDPOINT = settings.JAEGER_OTLP_HTTP_ENDPOINT
    SERVICE = settings.JAEGER_SERVICE_NAME

    logger.info("🔧 Setting up OpenTelemetry tracer")

    resource = Resource(attributes={SERVICE_NAME: SERVICE})
    tracer_provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(tracer_provider)

    try:
        # Choose the exporter based on the mode
        if MODE == "otlp-http":
            exporter = OTLPSpanExporterHTTP(endpoint=OTLP_HTTP_ENDPOINT)
        else:
            exporter = OTLPSpanExporterGRPC(endpoint=OTLP_GRPC_ENDPOINT, insecure=True)

        span_processor = BatchSpanProcessor(exporter)
        tracer_provider.add_span_processor(span_processor)

        if log_correlation:
            LoggingInstrumentor().instrument(set_logging_format=True)

        # Instrument the FastAPI app if not already instrumented
        if not FastAPIInstrumentor().is_instrumented_by_opentelemetry:
            FastAPIInstrumentor.instrument_app(app, tracer_provider=tracer_provider)

        logger.success(f"✅ Tracer initialized in {MODE.upper()} mode for {SERVICE}")

    except Exception as e:
        logger.exception(f"❌ Failed to set up tracer: {e}")
# REMOVED FOR TEST COVERAGE REASONS 😂