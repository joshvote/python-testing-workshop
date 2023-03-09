from typing import Optional

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, noload, selectinload

from .db import User


def get_user_by_id(conn_str, id: int) -> Optional[User]:
    """Gets user with specific ID

    please don't use this in prod. It doesn't consider anything about the connection lifecycle"""
    engine = create_engine(conn_str)
    with Session(engine) as session:
        stmt = (select(User).filter(User.user_id == id).options(noload(User.addresses)))
        return session.scalars(stmt).one_or_none()


def get_user_by_id_dependency_injected(session: Session, id: int) -> Optional[User]:
    """Gets user with specific ID (using a DI style pattern)

    This version allows the injection of Session that is managed elsewhere"""
    stmt = (select(User).filter(User.user_id == id).options(noload(User.addresses)))
    return session.scalars(stmt).one_or_none()


def get_all_users_with_addresses(conn_str) -> list[User]:
    """Gets all users with their addresses

    please don't use this in prod. It doesn't consider anything about the connection lifecycle"""
    engine = create_engine(conn_str)
    with Session(engine) as session:
        stmt = (select(User).order_by(User.user_id).options(selectinload(User.addresses)))
        return session.scalars(stmt).all()
