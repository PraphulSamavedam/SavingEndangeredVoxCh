import io
import requests
from datetime import datetime, timedelta
import time
import json
from PIL import Image
import numpy as np
from secrets import RED_API_TOKEN, NASA_API_KEY
from constants import ENDANGERED_SPECIES_FILE, REDLIST_API_BASE_URL, \
    GBIF_API_BASE_URL, NASA_BASE_URL


def read_json_file(file_path):
    """This function read the json file in right format"""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: '{file_path}' contains invalid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None


def get_species_locations(scientific_name, base_url=GBIF_API_BASE_URL):
    """
    This function returns the list of [latitude and longitudes] based on the
    scientific name of the specie specified.
    :param scientific_name: str Scientific Name of the
    :param base_url:
    :return:
    """
    params = {
        "scientificName": scientific_name,
        "hasCoordinate": True,
        "limit": 300  # Adjust this number based on how many records you want
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        locations = []
        for result in data.get('results', []):
            lat = result.get('decimalLatitude')
            lon = result.get('decimalLongitude')
            if lat is not None and lon is not None:
                locations.append((lat, lon))
        return locations
    else:
        print(
            f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None


def __get_endangered_species(token, base_url: str = REDLIST_API_BASE_URL):
    """
    This function fetches the endangered species data from IUCN RedList data
    through their API
    """

    all_species = []
    page = 0

    while True:
        url = f"{base_url}/species/page/{page}?token={token}"
        print(f"Fetching {page + 1} page data")
        response = requests.get(url=url)

        if response.status_code == 200:
            data = response.json()
            species_list = data.get('result', [])

            if not species_list:
                break

            all_species.extend(species_list)
            page += 1

            # Respect rate limiting
            time.sleep(2)
        else:
            print(f"Error: {response.status_code}")
            break

    return all_species


def populate_endangered_data():
    endangered_species = __get_endangered_species(RED_API_TOKEN)
    print(f"Total endangered species found: {len(endangered_species)}")

    with open(ENDANGERED_SPECIES_FILE, 'a') as file:
        json.dump(endangered_species, file)

    print(
        f"Successfully saved the endangered species to {ENDANGERED_SPECIES_FILE}")


def get_habitat(endangered_specie: str, base_url=REDLIST_API_BASE_URL,
                token=RED_API_TOKEN):
    habitats = []
    url = f"{base_url}/habitats/species/name/{endangered_specie}?token=" \
          f"{token}"
    print(f"url: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        habitat = data.get('result', {})

        if not habitat:
            print(f"Success API but no habitat data")
    else:
        print(f"Error: {response.status_code}")

    # Collect the habitat information
    for habit in habitat:
        habitats.append(habit['habitat'])
    return habitats


def get_satellite_imagery(lat, lon, start_date, end_date,
                          api_key=NASA_API_KEY, base_url=NASA_BASE_URL):
    """
    Retrieve satellite imagery for a given location over a time period using NASA API.
    :param base_url: NASA BASE URL
    :param lat: Latitude of the location
    :param lon: Longitude of the location
    :param start_date: Start date for the imagery (YYYY-MM-DD)
    :param end_date: End date for the imagery (YYYY-MM-DD)
    :param api_key: NASA API key (default is DEMO_KEY)
    :return: List of tuples containing (date, image)
    """
    image_data = []
    current_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    while current_date <= end_date:
        date_str = current_date.strftime('%Y-%m-%d')
        # Create the request URL
        params = {
            'lon': lon,
            'lat': lat,
            'date': date_str,
            'dim': 0.15,  # This sets the image dimension to 0.15 degrees
            'api_key': api_key
        }
        # Make the API request
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            # Save the image
            image = Image.open(io.BytesIO(response.content))
            image_data.append((date_str, image))
            print(f'Image retrieved for {date_str}')
        else:
            print(
                f'Error fetching image for {date_str}: {response.status_code} - {response.text}')
        current_date += timedelta(
            days=16)  # Landsat 8 has a 16-day repeat cycle
    return image_data


def calculate_ndvi(image):
    """
    Calculate NDVI from the image.
    This is a simplified calculation and may not be accurate for all image types.
    """
    img_array = np.array(image)
    # Assuming the image is in RGB format where Red is NIR and Blue is Red
    nir = img_array[:, :, 0].astype(float)
    red = img_array[:, :, 2].astype(float)
    ndvi = (nir - red) / (
            nir + red + 1e-8)  # Add small constant to avoid division by zero
    return ndvi
