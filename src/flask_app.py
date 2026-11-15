"""A9 Flask auto-instrumentation plus manual business spans."""

import os

from flask import Flask, jsonify
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


def create_app() -> Flask:
    """Create the demo service and configure OTLP tracing when enabled.

    The application keeps OTLP enabled by default. Tests set
    ``A9_OTLP_ENABLED=0`` so they exercise HTTP behavior without requiring a
    running Collector.
    """
    provider = TracerProvider()
    otlp_enabled = os.getenv("A9_OTLP_ENABLED", "1").lower() not in {
        "0",
        "false",
        "no",
    }
    if otlp_enabled:
        provider.add_span_processor(
            BatchSpanProcessor(
                OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
            )
        )
    trace.set_tracer_provider(provider)
    app = Flask(__name__)
    FlaskInstrumentor().instrument_app(app, tracer_provider=provider)
    tracer = trace.get_tracer("a9-flask-business", "1.0.0")

    @app.get("/checkout")
    def checkout():
        """Normal request with two manual business spans."""
        with tracer.start_as_current_span("checkout") as checkout_span:
            checkout_span.set_attribute("checkout.result", "paid")
            with tracer.start_as_current_span("charge-card") as payment_span:
                payment_span.set_attribute("payment.result", "approved")
        return jsonify({"status": "paid"})

    @app.get("/checkout/error")
    def checkout_error():
        """Controlled error used to demonstrate exception telemetry."""
        with tracer.start_as_current_span("checkout") as checkout_span:
            try:
                with tracer.start_as_current_span("charge-card"):
                    raise RuntimeError("demo payment gateway timeout")
            except RuntimeError as exc:
                checkout_span.record_exception(exc)
                checkout_span.set_status(trace.Status(trace.StatusCode.ERROR, str(exc)))
                return jsonify({"error": "payment gateway timeout"}), 500

    return app


if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=8080, use_reloader=False)
