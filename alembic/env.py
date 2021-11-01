from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context
from app.db.base import Base
from app.settings.settings import settings

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata


def run_migrations_online() -> None:
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = settings.POSTGRES_URL
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
