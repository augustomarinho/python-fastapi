import uvicorn
from fastapi import FastAPI
from fastapi_healthcheck import HealthCheckFactory, healthCheckRoute

from app.adapters.api.book import BookV1API

app = FastAPI()


def create_health_route():
    # Add Health Checks
    _healthChecks = HealthCheckFactory()
    app.add_api_route("/health", endpoint=healthCheckRoute(factory=_healthChecks))


def create_routes():
    BookV1API(app)


def start():
    create_health_route()
    create_routes()
    uvicorn.run(app, host="0.0.0.0", port=8383)


if __name__ == "__main__":
    start()
