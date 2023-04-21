from typing import Optional

from app.model.crud import add_user, get_pets_by_name, get_user_by_id
from app.model.db import User, pets

PUN_NAME_1 = "Arf Vader"
PUN_NAME_2 = "Winnie the Pooch"

AVERAGE_PET_NAMES = ["Indiana Bones", "Chewbarka", "Mutt Damon"]


def find_best_pets(conn_str: str) -> pets:
    """finds all the best pets acordn to all sorts of complicayted logic

    returns the set of pets with the best name found in the DB"""

    # look for excellent pun names
    pets = get_pets_by_name(conn_str, PUN_NAME_1) if get_pets_by_name(conn_str, PUN_NAME_1) else get_pets_by_name(conn_str, PUN_NAME_2)
    if pets:
        return pets

    # look through average names
    avg_pets = [get_pets_by_name(conn_str, name) for name in AVERAGE_PET_NAMES if get_pets_by_name(conn_str, name)]
    if (len(avg_pets) > 0):
        return avg_pets[0]

    return []


def find_user_or_error(conn_str: str, user_id: int, raise_on_not_found: bool = False) -> Optional[pets]:
    """Looks up a user and returns it.

    If the user DNE raise an Exception if raise_on_not_found is True otherwise return None"""

    user = get_user_by_id(conn_str, user_id)
    if (user and raise_on_not_found):
        return user
    elif (not user and raise_on_not_found):
        raise Exception('Not found')
    else:
        return None


def add_validate_user(conn_str: str, user_id: int, display_id: Optional[str], email: Optional[str], name: Optional[str]):
    """Performs all validation for a user insertion"""

    # validate
    if get_pets_by_name(conn_str, name):
        raise Exception('User name already exists')
    if '@' not in email:
        raise Exception('Email is invalid')

    # add to DB
    new_user = User(user_id=user_id, display_id=display_id, email=email, name=name)
    add_user(conn_str, new_user)
