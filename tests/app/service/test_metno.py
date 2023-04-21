import json
import unittest.mock as mock
from typing import Optional

from app.service.metno import get_location_forecast


class MockException(Exception):
    pass


class FakeHttpException(Exception):
    pass

@mock.patch("app.service.metno.requests")
def test_get_location_forecast(mock_requests: mock.MagicMock):
    """Tests that a typical response is parsed without errors"""

    # Arrange

    # mock out the outgoing request to return fixed JSON
    with open("tests/example_data/metno_midday.json") as f:
        json_response_data = json.loads(f.read())

    extracted_uri: Optional[str] = None

    def mocked_get(endpoint: str, headers: dict[str, str]):
        nonlocal extracted_uri

        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        extracted_uri = endpoint
        return MockResponse(json_response_data, 200)
    mock_requests.get = mock.Mock(side_effect=mocked_get)

    # Act
    forecast = get_location_forecast({"latitude": 20, "longitude": 30, "altitude": 40})

    # Assert
    mock_requests.get.assert_called_once()
    assert extracted_uri, "extracted_uri should've been set in mocked_get"
    assert extracted_uri.find("lat=20") > 0, f"Latitude not present in the outgoing URI {extracted_uri}"
    assert extracted_uri.find("lon=30") > 0, f"Longitude not present in the outgoing URI {extracted_uri}"
    assert extracted_uri.find("altitude=40") > 0, f"Altitude not present in the outgoing URI {extracted_uri}"

    # Quick check on the response schema
    assert forecast
    assert type(forecast) == dict
    assert forecast["type"] == "Feature"
    assert "geometry" in forecast
    assert "properties" in forecast


@mock.patch("app.service.metno.requests")
def test_get_location_forecast_handles_http_error(mock_requests: mock.MagicMock):
    """Tests that http error is handled gracefully"""

    # Arrange

    # mock the response to return a HTTP 500
    def mocked_get(endpoint: str, headers: dict[str, str] = None):

        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                raise MockException('This shouldnt be called')
        return MockResponse('This is a mocked error response', 500)
    mock_requests.get = mock.Mock(side_effect=mocked_get)

    # Act
    forecast = get_location_forecast({"latitude": 20, "longitude": 30, "altitude": 40})

    # Assert
    mock_requests.get.assert_called_once()
    assert forecast is None


@mock.patch("app.service.metno.requests")
def test_get_location_forecast_handles_exception(mock_requests: mock.MagicMock):
    """Tests that http error is handled gracefully"""

    # Arrange

    # mock the response to just raise an exception
    mock_requests.get = mock.Mock(side_effect=FakeHttpException('Expected exception'))

    # Act
    try:
        get_location_forecast({"latitude": 20, "longitude": 30, "altitude": 40})
        assert False, "Expected a FakeHttpException to be raised"
    except FakeHttpException:
        pass

    # Assert
    mock_requests.get.assert_called_once()
