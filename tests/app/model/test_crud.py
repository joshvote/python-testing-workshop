from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.model.crud import get_all_users_with_addresses, get_user_by_id, get_user_by_id_dependency_injected


def test_get_user_by_id_di(pg_base_config):
    engine = create_engine(pg_base_config)
    with Session(engine) as session:
        u1 = get_user_by_id_dependency_injected(session, 1)
        assert u1.name == 'user 1'
        assert u1.display_id == 'u1'
        assert u1.email == 'user1@test.com'
        assert len(u1.addresses) == 0, "Addresses will be zero because this function does NOT load Addresses"


def test_get_user_by_id(pg_base_config):
    """Tests getting a user by a specific ID"""
    u1 = get_user_by_id(pg_base_config, 1)
    u3 = get_user_by_id(pg_base_config, 3)

    assert u1.name == 'user 1'
    assert u1.display_id == 'u1'
    assert u1.email == 'user1@test.com'
    assert len(u1.addresses) == 0, "Addresses will be zero because this function does NOT load Addresses"

    assert u3.name == 'user 3'
    assert u3.display_id == 'u3'
    assert u3.email == 'user3@test.com'
    assert len(u3.addresses) == 0, "Addresses will be zero because this function does NOT load Addresses"

    # test out of range values
    assert get_user_by_id(pg_base_config, 0) is None
    assert get_user_by_id(pg_base_config, -1) is None
    assert get_user_by_id(pg_base_config, 4) is None
    assert get_user_by_id(pg_base_config, 999999999999) is None


def test_get_all_users_with_addresses(pg_base_config):
    """Validates get_all_users operates on the basic set of users"""

    all_users = get_all_users_with_addresses(pg_base_config)
    assert len(all_users) == 3, f"Base config has 3 users, got {len(all_users)} instead"

    # User 1
    assert all_users[0].name == 'user 1'
    assert all_users[0].display_id == 'u1'
    assert all_users[0].email == 'user1@test.com'
    assert len(all_users[0].addresses) == 2
    assert all_users[0].addresses[0].address_line1 == '1 Fake St'
    assert all_users[0].addresses[0].address_line2 == 'Suburb 1'
    assert all_users[0].addresses[0].is_primary is False
    assert all_users[0].addresses[1].address_line1 == '2 Fake St'
    assert all_users[0].addresses[1].address_line2 == 'Suburb 2'
    assert all_users[0].addresses[1].is_primary is True

    # User 2
    assert all_users[1].name == 'user 2'
    assert all_users[1].display_id == 'u2'
    assert all_users[1].email == 'user2@test.com'
    assert len(all_users[1].addresses) == 1
    assert all_users[1].addresses[0].address_line1 == '3 Fake St'
    assert all_users[1].addresses[0].address_line2 == 'Suburb 3'
    assert all_users[1].addresses[0].is_primary is False

    # User 3
    assert all_users[2].name == 'user 3'
    assert all_users[2].display_id == 'u3'
    assert all_users[2].email == 'user3@test.com'
    assert len(all_users[2].addresses) == 0
