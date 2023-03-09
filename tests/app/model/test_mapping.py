from app.model.db import Address, User
from app.model.mapping import map_user_from_view, map_user_to_view
from app.model.view import ViewUser


def test_map_user_to_view():
    """This test can be greatly improved with a bit of reflection and "auto generation" of the input objects
    such that they all include unique property names.

    You could even go one step further and automate the checking of property -> property by name matching
    with reflection to ensure coverage for future expansions to the model"""

    # Arrange
    db_user_2_addr = User(
        user_id=1,
        display_id='id-2',
        email='email-3',
        name='name-4',
        addresses=[
            Address(address_id=2, is_primary=False, address_line1='al1', address_line2='al2'),
            Address(address_id=3, is_primary=True, address_line1='al3', address_line2='al4'),
        ]
    )

    db_user_no_addr = User(
        user_id=4,
        display_id='id-5',
        email='email-6',
        name='name-7',
        addresses=[]
    )

    # Act
    view_user_with_addr = map_user_to_view(db_user_2_addr)
    view_user_no_addr = map_user_to_view(db_user_no_addr)

    # Assert
    assert view_user_with_addr.display_id == db_user_2_addr.display_id
    assert view_user_with_addr.email == db_user_2_addr.email
    assert view_user_with_addr.name == db_user_2_addr.name
    assert view_user_with_addr.primary_address_line1 == db_user_2_addr.addresses[1].address_line1  # first primary
    assert view_user_with_addr.primary_address_line2 == db_user_2_addr.addresses[1].address_line2  # first primary

    assert view_user_no_addr.display_id == db_user_no_addr.display_id
    assert view_user_no_addr.email == db_user_no_addr.email
    assert view_user_no_addr.name == db_user_no_addr.name
    assert view_user_no_addr.primary_address_line1 is None
    assert view_user_no_addr.primary_address_line2 is None


def test_map_user_from_view():
    """This test can be greatly improved with a bit of reflection and "auto generation" of the input objects
    such that they all include unique property names.

    You could even go one step further and automate the checking of property -> property by name matching
    with reflection to ensure coverage for future expansions to the model"""
    # Arrange
    view_user_no_addr = ViewUser(
        email='email-1',
        display_id='display_id-1',
        name='name-1',
        primary_address_line1=None,
        primary_address_line2=None
    )

    view_user_with_addr = ViewUser(
        email='email-2',
        display_id='display_id-2',
        name='name-2',
        primary_address_line1='al3',
        primary_address_line2='al4'
    )

    # Act
    db_user_no_addr = map_user_from_view(view_user_no_addr)
    db_user_with_addr = map_user_from_view(view_user_with_addr)

    # Assert
    assert db_user_no_addr.user_id is None, 'This should not be specified by the view - the DB will handle this'
    assert db_user_no_addr.name == view_user_no_addr.name
    assert db_user_no_addr.display_id == view_user_no_addr.display_id
    assert db_user_no_addr.email == view_user_no_addr.email
    assert len(db_user_no_addr.addresses) == 0

    assert db_user_with_addr.user_id is None, 'This should not be specified by the view - the DB will handle this'
    assert db_user_with_addr.name == view_user_with_addr.name
    assert db_user_with_addr.display_id == view_user_with_addr.display_id
    assert db_user_with_addr.email == view_user_with_addr.email
    assert len(db_user_with_addr.addresses) == 1
    assert db_user_with_addr.addresses[0].address_id is None, 'This should not be specified by the view'
    assert db_user_with_addr.addresses[0].user_id is None, 'This should not be specified by the view'
    assert db_user_with_addr.addresses[0].address_line1 == view_user_with_addr.primary_address_line1
    assert db_user_with_addr.addresses[0].address_line2 == view_user_with_addr.primary_address_line2
    assert db_user_with_addr.addresses[0].is_primary is True
