import unittest.mock as mock

from app.model.business_logic import find_best_pets
from app.model.db import pets


@mock.patch("app.model.business_logic.get_pets_by_name")
def test_find_best_pets(mock_get_pets_by_name: mock.MagicMock):
    """Tests the flows for fetching pets"""
    conn_str = "fake-conn-str"
    expected_response = [pets(Name="Bob")]
    mock_get_pets_by_name.return_value = expected_response

    assert find_best_pets(conn_str) is expected_response
