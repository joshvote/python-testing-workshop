from typing import Any, Optional

from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import Session, noload, selectinload

from .db import User, pets


def get_user_by_id(conn_str: str, id: int) -> Optional[User]:
    """Gets user with specific ID

    please don't use this in prod. It doesn't consider anything about the connection lifecycle"""
    engine = create_engine(conn_str)
    with Session(engine) as session:
        stmt = (select(User).filter(User.user_id == id).options(noload(User.addresses)))
        return session.scalars(stmt).one_or_none()


def add_user(conn_str: str, user: User):
    """Adds user to the database

    please don't use this in prod. It doesn't consider anything about the connection lifecycle"""
    engine = create_engine(conn_str)
    with Session(engine) as session:
        session.add(user)
        session.commit()


def get_user_by_id_dependency_injected(session: Session, id: int) -> Optional[User]:
    """Gets user with specific ID (using a DI style pattern)

    This version allows the injection of Session that is managed elsewhere"""
    stmt = (select(User).filter(User.user_id == id).options(noload(User.addresses)))
    return session.scalars(stmt).one_or_none()


def get_all_users_with_addresses(conn_str: str) -> list[User]:
    """Gets all users with their addresses

    please don't use this in prod. It doesn't consider anything about the connection lifecycle"""
    engine = create_engine(conn_str)
    with Session(engine) as session:
        stmt = (select(User).order_by(User.user_id).options(selectinload(User.addresses)))
        return session.scalars(stmt).all()


def get_pets_by_name(conn_str: str, name: str) -> list[pets]:
    """Gets all pets by name"""

    # WIP
    # with Session(engine) as session:
    #     stmt = (select(pet).order_by(pet.user_id).options(selectinload(User.addresses)))
    #     return session.scalars(stmt).all()

    engine = create_engine(conn_str)
    with Session(engine) as session:
        stmt = text("SELECT * FROM \"Pets\" WHERE name = '{name}'")
        return session.scalars(stmt).all()


def get_users_by_name(conn_str: str, name: str) -> list[pets]:
    """Gets all users by name"""

    engine = create_engine(conn_str)
    with Session(engine) as session:
        stmt = text("SELECT * FROM \"user\" WHERE name = '{name}'")
        return session.scalars(stmt).all()


def get_pet_default(conn_str: str, pet_id, default_pet_name: dict[str, Any] = {"Name": "Barry"}) -> pets:
    """Gets all users with their addresses"""
    engine = create_engine(conn_str)
    with Session(engine) as session:
        stmt = (select(pets).filter(pets.PetId == pet_id))
        out = session.scalars(stmt).one_or_none()
        if out == None:
            return pets(**default_pet_name)
        return out
