import geopandas as gpd
import numpy as np


# Read the GeoJSON file into a GeoDataFrame
gdf = gpd.read_file(r'C:\Users\ciara\OneDrive\Documents\GitHub\Squamish_plants_map\withID.geojson')


# counts species of given name
def species_count(species, data):
    count = 0
    for index, row in data.iterrows():
        if species == row['feature_collection_name']:
            count = count + 1
    print(count)
    return(count)
    
# adds count to new count column (righ tnow ID)
def add_count(species, data):
    for index, row in gdf.iterrows():
        if species == row['feature_collection_name']:
            gdf.loc[index, 'ID'] = species_count(species, data)
        #print("Count:", count)  # Output the count

species_count("Achillea_millefolium", gdf)

gdf.to_file('plant_species_cleaned.geojson', driver='GeoJSON')

