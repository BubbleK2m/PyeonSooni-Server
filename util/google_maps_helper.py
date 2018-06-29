from app import app
from googlemaps import Client


def get_location_data_from_address(address):
    # generate api client from flask app config
    google_maps = app.config['GOOGLE_MAPS']
    google_maps_client = Client(key=google_maps['api_key'])

    # get geocode results
    geocode_results = google_maps_client.geocode(address)

    # cannot found geocode results, we'll return none
    if len(geocode_results) == 0:
        return None

    # get first item from google geocodes
    geocode_result = geocode_results[0]

    # get items about location
    location_dict = geocode_result['geometry']['location']

    # get latitude and longitude from location dict
    location_data = {
        'lat': location_dict['lat'],
        'lng': location_dict['lng']
    }

    return location_data
