const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const app = express();
const PORT = 3000;

app.use(bodyParser.json());
app.use(express.static('Squamish_Access_liz')); // Serve static files from the 'Squamish_Access_liz' directory

// Endpoint to handle survey submissions
app.post('/submit-survey', (req, res) => {
    const submission = req.body;

    // Load existing GeoJSON file
    let geojson = {
        "type": "FeatureCollection",
        "features": []
    };

    if (fs.existsSync('form_data.geojson')) {
        geojson = JSON.parse(fs.readFileSync('form_data.geojson', 'utf8'));
    }

    // Create a new GeoJSON feature from the submission
    let newFeature;

    if (submission.type === 'Point') {
        // Submission is a point
        newFeature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [submission.longitude, submission.latitude]
            },
            "properties": {
                "description": submission.description,
                "time": submission.time,
                "notes": submission.notes,
                "picture": submission.picture,
                // Add other properties as needed
            }
        };
    } else if (submission.type === 'Polygon') {
        // Submission is a polygon
        newFeature = {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": submission.coordinates // Assuming coordinates is an array of linear rings (arrays of positions)
            },
            "properties": {
                "description": submission.description,
                "time": submission.time,
                "notes": submission.notes,
                "picture": submission.picture,
                // Add other properties as needed
            }
        };
    } else {
        return res.status(400).json({ message: 'Invalid geometry type' });
    }

    // Add the new feature to the GeoJSON object
    geojson.features.push(newFeature);

    // Save the updated GeoJSON file
    fs.writeFileSync('form_data.geojson', JSON.stringify(geojson, null, 2));

    res.json({ message: 'Submission saved!' });
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
