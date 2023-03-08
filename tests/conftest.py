import os

import alembic.config
import pytest


def _generate_conn_str_from_database(db):
    """Utility for extracting a connection string"""
    cps = db.pgconn
    return f"postgresql://{cps.user.decode('UTF-8')}@{cps.host.decode('UTF-8')}:{cps.port.decode('UTF-8')}/{cps.db.decode('UTF-8')}"


@pytest.fixture
def pg_database(postgresql):
    """Set up the testing DB and applies the current migrations and loads the base config"""
    cwd = os.getcwd()
    print(cwd)
    try:
        os.chdir('./app/')
        alembicArgs = [
            '--raiseerr',
            '-xtest.database.url=' + _generate_conn_str_from_database(postgresql),
            'upgrade', 'head',
        ]
        alembic.config.main(argv=alembicArgs)
    finally:
        os.chdir(cwd)

    with open("tests/example_sql/base_config.sql") as f:
        base_config_sql = f.read()

    with postgresql.cursor() as cursor:
        cursor.execute(base_config_sql)
        postgresql.commit()

    yield postgresql


@pytest.fixture
def pg_base_config(pg_database):
    """Basic test environment that will setup the base config and return the connection string"""
    yield _generate_conn_str_from_database(pg_database)
