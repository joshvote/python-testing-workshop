from app.model.crud import get_pets_by_name
from app.model.db import pets

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
