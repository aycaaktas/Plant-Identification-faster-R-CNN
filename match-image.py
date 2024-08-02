import pandas as pd
import os

class Plant:
    def __init__(self, image_name, organ, species_id, obs_id, license, partner, gbif_species_id, species, genus, family, learn_tag, image_path=None):
        self.image_name = image_name
        self.organ = organ
        self.species_id = species_id
        self.obs_id = obs_id
        self.license = license
        self.partner = partner
        self.gbif_species_id = gbif_species_id
        self.species = species
        self.genus = genus
        self.family = family
        self.learn_tag = learn_tag
        self.image_path = image_path  # New attribute to store the path of the image


# Assuming the Excel file is named 'plant_data.xlsx' and is in the current directory
file_path = '/home/aycaaktas/PURE/PlantCLEF2024singleplanttrainingdata.csv'
df = pd.read_csv(file_path, delimiter=';')

  


# Directory where images are stored
image_directory_path = '/home/aycaaktas/PURE/DATA/images_max_side_800'

# List to store Plant objects
plants = []

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    species_folder_path = os.path.join(image_directory_path, str(row['species_id']))
    image_file_path = os.path.join(species_folder_path, row['image_name'])
    
    # Check if the image file exists in the specified path
    if os.path.exists(image_file_path):
        plant = Plant(
            image_name=row['image_name'],
            organ=row['organ'],
            species_id=row['species_id'],
            obs_id=row['obs_id'],
            license=row['license'],
            partner=row['partner'],
            gbif_species_id=row['gbif_species_id'],
            species=row['species'],
            genus=row['genus'],
            family=row['family'],
            learn_tag=row['learn_tag'],
            image_path=image_file_path  # Storing the image path
        )
        plants.append(plant)
    else:
        # You might want to handle cases where the image doesn't exist
        print(f"Image {row['image_name']} not found in {species_folder_path}")

# Example: Print out details of the first few Plant objects to verify
for plant in plants[:5]:  # Just as an example, print details of first 5 plants
    print(f"Species ID: {plant.species_id}, Image: {plant.image_name}, Image Path: {plant.image_path}")
