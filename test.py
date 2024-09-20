import requests


def get_species_locations(scientific_name):
    base_url = "https://api.gbif.org/v1/occurrence/search"

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


# Example usage
# scientific_name = "Panthera tigris"  # Replace with your species of interest
scientific_name = "Aaadonta angaurana"
locations = get_species_locations(scientific_name)

if locations:
    print(f"Locations for {scientific_name}:")
    for i, (lat, lon) in enumerate(locations, 1):
        print(f"{i}. Latitude: {lat}, Longitude: {lon}")
else:
    print("No location data available or error occurred.")