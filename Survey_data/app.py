from flask import Flask, request, render_template
import json
import os

app = Flask(__name__, template_folder='Scripts')

# Ensure the GeoJSON file exists with the correct structure
def initialize_geojson_file():
    with open('responses.geojson', 'w') as f:
        json.dump({"type": "FeatureCollection", "features": []}, f, indent=2)

@app.route('/')
def index():
    return render_template('community_entry_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    print("Form submitted!")  # Debugging line
    name = request.form.get('name')
    description = request.form.get('description')
    observation_time = request.form.get('observation-time')
    location_coordinates = request.form.get('location-coordinates')
    geometry_type = request.form.get('geometry-type')  # New field for geometry type
    notes = request.form.get('notes')
    picture = request.files.get('picture')

    # Check if the GeoJSON file exists and is not empty
    if not os.path.exists('responses.geojson') or os.path.getsize('responses.geojson') == 0:
        initialize_geojson_file()

    # Load existing GeoJSON data
    with open('responses.geojson', 'r') as f:
        try:
            geojson_data = json.load(f)
        except json.JSONDecodeError:
            initialize_geojson_file()
            with open('responses.geojson', 'r') as f:
                geojson_data = json.load(f)

    # Create a new GeoJSON feature based on the geometry type
    if geometry_type == 'Point':
        geometry = {
            "type": "Point",
            "coordinates": json.loads(location_coordinates)  # Ensure it's in [longitude, latitude]
        }
        
    else:
        return "Invalid geometry type!", 400  # Handle invalid geometry type

    feature = {
        "type": "Feature",
        "properties": {
            "name": name,
            "description": description,
            "observation_time": observation_time,
            "notes": notes
        },
        "geometry": geometry
    }

    # Add the new feature to the GeoJSON data
    geojson_data['features'].append(feature)

    # Save the updated GeoJSON data back to the file
    with open('responses.geojson', 'w') as f:
        json.dump(geojson_data, f, indent=2)

    # Handle picture upload if necessary
    if picture:
        if not os.path.exists('uploads'):
            os.makedirs('uploads')
        picture.save(os.path.join('uploads', picture.filename))

    return "Thank you for your submission!"

if __name__ == '__main__':
    # Initialize the GeoJSON file if it doesn't exist
    if not os.path.exists('responses.geojson'):
        initialize_geojson_file()
    app.run(debug=True)
