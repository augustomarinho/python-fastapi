from dependency_injector import containers, providers
from sqlalchemy import create_engine, URL

from app.adapters.repositories.book_repository import BookRepository
from app.configs.settins import get_db_settings


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["app.adapters.entrypoints.http.v1.book_router",
                                                            "app.adapters.entrypoints.http.v1.settings_router"])

    config = providers.Configuration()
    config.from_dict(get_db_settings().model_dump())

    db_engine = providers.Singleton(
        create_engine,
        URL.create(
            drivername="postgresql",
            username=config.get("db_user"),
            password=config.get("db_password"),
            host=config.get("db_host"),
            port=config.get("db_port"),
            database=config.get("db_name"),
        ),
        isolation_level="AUTOCOMMIT",
    )

    book_port = providers.Factory(BookRepository, db=db_engine)