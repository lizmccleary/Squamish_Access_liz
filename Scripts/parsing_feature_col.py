import geopandas as gpd
import pandas as pd
import numpy as np
import requests
import os
import glob


###################### reading geojson directory and combining feature collections into single JSON file ###########################################

# Directory containing GeoJSON files
directory = r'C:\Users\ciara\OneDrive\Documents\GitHub\Exploratory-Lab-1\Squamish_Nation_plants'

# Get a list of all GeoJSON files in the directory
geojson_files = glob.glob(os.path.join(directory, '*.geojson'))


species_list = []
gdfs = []
# Iterate over each GeoJSON file and load it into GeoDataFrame
for file in geojson_files:
    feature_collection_name = os.path.splitext(os.path.basename(file))[0]
    ID= 0
    species_count = 0

    gdf = gpd.read_file(file)
    gdf["ID"] = ID
    gdf["species_count"] = species_count
    gdf['feature_collection_name'] = feature_collection_name
    ## adding all species names to a list for later
    species_list.append(feature_collection_name)
    print(species_list)
    
    # Append GeoDataFrame to list
    gdfs.append(gdf)


combined_gdf = gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True))

output_geojson_file = 'withID.geojson'

# Export to JSON
combined_gdf.to_file(output_geojson_file, driver='GeoJSON')

print(combined_gdf.head())
# Read the GeoJSON file into a GeoDataFrame
gdf = gpd.read_file(r'C:\Users\ciara\OneDrive\Documents\GitHub\Exploratory-Lab-1\withID.geojson')


###################### adding ID column ######################
count = 1

# Adding ID column using count
for index, row in gdf.iterrows():
    count = count + 1
    # Access and modify the value new ID property using .loc
    gdf.loc[index, 'ID'] = count
    #print(gdf.loc[index, 'ID'])

# Save as a new GeoJSON file
gdf.to_file('withID.geojson', driver='GeoJSON')



## adding species count ####################################################################
gdf = gpd.read_file(r'C:\Users\ciara\OneDrive\Documents\GitHub\Exploratory-Lab-1\withID.geojson')


# counts species of given name
def count_species(species, data):
    count = 0
    for index, row in data.iterrows():
        if species == row['feature_collection_name']:
            count = count + 1
    print(count)
    return(count)

# adds count to new count column (righ tnow ID)
for sp in species_list:
    for index, row in gdf.iterrows():
        if sp == row['feature_collection_name']:
            sp_count = count_species(sp, gdf)
            gdf.loc[index, 'species_count'] = str(sp_count)


gdf.to_file('withID.geojson', driver='GeoJSON')




