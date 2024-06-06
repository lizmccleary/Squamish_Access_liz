import json

def correct_coordinates(squamish_trails_geojson):
    # Open and read the GeoJSON file
    with open(squamish_trails_geojson, 'r') as f:
        data = json.load(f)
    
    # Iterate over features in the GeoJSON and correct coordinates
    for feature in data['features']:
        coordinates = feature['geometry']['coordinates']
        corrected_coordinates = []
        for coord in coordinates:
            # Correcting coordinates assuming they are in EPSG:26910 projection
            corrected_coord = [
                (coord[0] - 442625),  # Adjusting X-coordinate
                (coord[1] - 5428476)  # Adjusting Y-coordinate
            ]
            corrected_coordinates.append(corrected_coord)
        feature['geometry']['coordinates'] = corrected_coordinates
    
    # Write corrected data back to the GeoJSON file
    with open('/Users/lizmccleary/GitHub/Squamish_Access_liz/squamish_trails.geojson', 'w') as f:
        json.dump(data, f, indent=4)

# Usage
correct_coordinates('/Users/lizmccleary/GitHub/Squamish_Access_liz/squamish_trails.geojson')
