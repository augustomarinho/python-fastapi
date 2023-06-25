from typing import Callable, List, Any

from fastapi import APIRouter, FastAPI
from fastapi.datastructures import Default


class FastAPIRouter:
    def __init__(self, app: FastAPI):
        self.router = APIRouter()
        self.app = app

    def add_api_route(
        self,
        path: str,
        endpoint: Callable,
        methods: List[str] = None,
        response_model: Any = Default(None),
    ):
        self.router.add_api_route(
            path, endpoint, methods=methods, response_model=response_model
        )
        self.app.include_router(self.router)
