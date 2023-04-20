"""
Utility functions for accessing the Norwegian Meteorological Institute/NRK
weather service (https://www.yr.no/en)

API Documentation here:
https://developer.yr.no/doc/locationforecast/HowTO/
"""

import logging

import requests

logger = logging.getLogger(__name__)

FORECAST_API_URL = (
    "https://api.met.no/weatherapi/locationforecast/2.0/"
    "{forecast_type}?lat={lat}&lon={lon}&altitude={altitude}"
)


def get_location_forecast(
        location: dict,
        forecast_type: str = "compact"
        ) -> dict:
    """
    args:
      location: dictionary containing "latitude", "longitude" and "altitude"
      forecast_type possible values "compact" or "complete"
    """
    endpoint = FORECAST_API_URL.format(
        forecast_type=forecast_type,
        lat=location["latitude"],
        lon=location["longitude"],
        altitude=location["altitude"],
    )
    headers = {"User-Agent": "bsgip.com mike.turner@anu.edu.au"}
    response = requests.get(endpoint, headers=headers, timeout=2)
    if response.status_code == 200:
        return response.json()
    else:
        logging.warning(response)
    return None
