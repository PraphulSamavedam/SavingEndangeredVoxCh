import os
from constants import ENDANGERED_SPECIES_FILE
from tmp.SavingEndangeredVoxCh.utils import (populate_endangered_data, read_json_file,
                                             get_species_locations, get_satellite_imagery,
                                             calculate_ndvi)
import numpy as np
from PIL import Image
def main():
    """
    This is the main function which is run when run as the main file.
    :return: None
    """
    if not os.path.exists(ENDANGERED_SPECIES_FILE):
        populate_endangered_data()

    file_path = ENDANGERED_SPECIES_FILE
    json_data = read_json_file(file_path)

    print(f"Analyzing {len(json_data)} data")
    scientific_name = json_data[0]['scientific_name']
    locations = get_species_locations(scientific_name)

    # MVP only the first location
    primary_location = locations[0]
    lat, lon = primary_location

    start_date = '2023-01-01'
    end_date = '2023-03-31'

    image_data = get_satellite_imagery(lat, lon, start_date, end_date)

    # Process and analyze the images
    for date, image in image_data:
        # Save the original image
        image.save(f'nasa_image_{date}.png')
        print(f'Saved image as nasa_image_{date}.png')
        # Calculate and save NDVI
        ndvi = calculate_ndvi(image)
        Image.fromarray((ndvi * 255).astype(np.uint8)).save(f'ndvi_{date}.png')
        print(f'Saved NDVI image as ndvi_{date}.png')
        # Print average NDVI
        print(f'Average NDVI for {date}: {np.mean(ndvi)}')


if __name__ == "__main__":
    main()
