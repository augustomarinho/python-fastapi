from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import create_async_engine

from app.adapters.repositories.book_repository import BookRepository
from app.configs.settins import get_db_settings


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["app.adapters.entrypoints.http.v1.book_router",
                                                            "app.adapters.entrypoints.http.v1.settings_router"])

    config = providers.Configuration()
    config.from_dict(get_db_settings().model_dump())

    db_engine = providers.Singleton(
        create_async_engine,
        config.get("db_dsn"),
        pool_size=config.get("db_max_pool_size"),
        max_overflow=config.get("db_overflow_size"),
        isolation_level="AUTOCOMMIT",
    )

    book_port = providers.Factory(BookRepository, db=db_engine)