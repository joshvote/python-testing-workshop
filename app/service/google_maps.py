import googlemaps
from datetime import datetime
import logging
from model.crud import get_all_users_with_addresses
import os
from model.db import Address

BSGIP_GOOGLE_MAPS_KEY = "HGDH-4JHG-9FDH-233G-9099-OOJG"
google_maps_key = os.environ["GOOGLE_MAPS_KEY"]
if google_maps_key == None:
    google_maps_key = BSGIP_GOOGLE_MAPS_KEY

gmaps = googlemaps.Client(key=google_maps_key)

def fetch_geocode(address):
    """Returns the geocode for an address.

    Args:
        address: The desired address

    Returns:
        a geocode
    """
    # Geocoding an address
    return gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

def fetch_directions(address1 : Address, address2:Address):
    """Returns the geocode for an address.

    Args:
        address: The desired address
    """
    now = datetime.now()
    print(now, address1, address2)
    directions_result=gmaps.directions(address1,address2,mode="transit",departure_time=now)

def validate(address: str):
    # Validate an address with address validation
    addressvalidation_result =  gmaps.addressvalidation([address], 
                                                        regionCode='US',
                                                        locality='Mountain View', 
                                                        enableUspsCass=True)
    return addressvalidation_result

def fetch_geocodes_for_all_users(connection: str) -> list:
    """Fetch geocodes of all users if user have address

    Args:
        connection: the connection string to connect to the database

    Returns:
        geocodes of users
    """
    users = get_all_users_with_addresses(connection)
    for user in users:
        geocode_results_for_all_users_with_addresses_first_only = []
        adr = user.addresses[0].address_line1
        geocode_results_for_all_users_with_addresses_first_only.append(adr)
    return geocode_results_for_all_users_with_addresses_first_only