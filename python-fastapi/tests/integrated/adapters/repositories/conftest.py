import asyncio

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from testcontainers.postgres import PostgresContainer


# https://github.com/pytest-dev/pytest-asyncio/issues/38
@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="module")
def postgres_container():
    with PostgresContainer("postgres:15.4") as container:
        # https://github.com/testcontainers/testcontainers-python/issues/263
        container.driver = "asyncpg"
        yield container


@pytest.fixture(scope="module")
def db_engine(postgres_container):
    db_uri = postgres_container.get_connection_url()
    return create_async_engine(db_uri, isolation_level="AUTOCOMMIT")


@pytest.fixture(scope="module")
def async_engine(event_loop, postgres_container, db_engine):
    db_uri = postgres_container.get_connection_url()

    # Set up Alembic configuration to use for tests
    alembic_config = Config()
    alembic_config.set_main_option("script_location", "infrastructure/alembic/migrations")
    alembic_config.set_main_option("sqlalchemy.url", db_uri)

    # Apply migrations
    command.upgrade(alembic_config, "head")

    yield db_engine

    event_loop.run_until_complete(db_engine.dispose())


@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown(event_loop, db_engine):
    async def setup():
        async with db_engine.connect() as conn:
            await conn.execute(text("TRUNCATE TABLE books RESTART IDENTITY"))

    yield None

    event_loop.run_until_complete(setup())
