from typing import Optional

from db import Address, User
from view import ViewUser


def map_user_to_view(db_user: User) -> ViewUser:
    """Converts a DB representation of a user into the view equivalent"""
    # find first non primary address
    first_primary_addr = next((a for a in db_user.addresses if a.is_primary), None)

    # map it to a simple string
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    if first_primary_addr is not None:
        address_line1 = first_primary_addr.address_line1
        address_line2 = first_primary_addr.address_line2

    return ViewUser(db_user.email, db_user.display_id, db_user.name, address_line1, address_line2)


def map_user_from_view(view_user: ViewUser) -> User:
    """Converts a view representation of a user into the database equivalent"""

    # map primary address back from string
    addresses: list[Address] = []
    if view_user.primary_address:
        # NOTE - we are ignoring ID mapping as part of this example. In the real world this would either
        #        use UUID's to sidestep this issue OR it would integrate an ID lookup step
        #
        #        we are also ignoring how the whole CRUD operations will function w.r.t updating/inserting
        addresses = [Address(address=view_user.primary_address, is_primary=True)]

    return User(
        display_id=view_user.display_id,
        email=view_user.email,
        name=view_user.name,
        addresses=addresses
    )
