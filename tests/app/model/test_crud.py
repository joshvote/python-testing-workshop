from app.model.crud import get_all_users_with_addresses, get_user_by_id


def test_get_user_by_id(pg_base_config):
    """Tests getting a user by a specific ID"""
    u1 = get_user_by_id(pg_base_config, 1)
    u3 = get_user_by_id(pg_base_config, 3)

    assert u1.name == 'user 1'
    assert u1.display_id == 'u1'
    assert u1.email == 'user1@test.com'
    assert len(u1.addresses) == 2
    assert u1.addresses[0].address == '1 Fake St'
    assert u1.addresses[0].is_primary is False
    assert u1.addresses[1].address == '2 Fake St'
    assert u1.addresses[1].is_primary is True

    assert u3.name == 'user 3'
    assert u3.display_id == 'u3'
    assert u3.email == 'user3@test.com'
    assert len(u3.addresses) == 0

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
    assert all_users[0].addresses[0].address == '1 Fake St'
    assert all_users[0].addresses[0].is_primary is False
    assert all_users[0].addresses[1].address == '2 Fake St'
    assert all_users[0].addresses[1].is_primary is True

    # User 2
    assert all_users[1].name == 'user 2'
    assert all_users[1].display_id == 'u2'
    assert all_users[1].email == 'user2@test.com'
    assert len(all_users[1].addresses) == 1
    assert all_users[1].addresses[0].address == '3 Fake St'
    assert all_users[1].addresses[0].is_primary is False

    # User 3
    assert all_users[2].name == 'user 3'
    assert all_users[2].display_id == 'u3'
    assert all_users[2].email == 'user3@test.com'
    assert len(all_users[2].addresses) == 0
