document.getElementById('geometry-type').addEventListener('change', function() {
    const geometryType = this.value;
    if (geometryType === 'Point') {
        document.getElementById('point-inputs').style.display = 'block';
        document.getElementById('polygon-inputs').style.display = 'none';
    } else if (geometryType === 'Polygon') {
        document.getElementById('point-inputs').style.display = 'none';
        document.getElementById('polygon-inputs').style.display = 'block';
    }
});

document.getElementById('survey_form').addEventListener('submit', function(event) {
    event.preventDefault();

    const geometryType = document.getElementById('geometry-type').value;
    let geometry;

    if (geometryType === 'Point') {
        const latitude = parseFloat(document.getElementById('latitude').value);
        const longitude = parseFloat(document.getElementById('longitude').value);
        geometry = {
            type: 'Point',
            coordinates: [longitude, latitude]
        };
    } else if (geometryType === 'Polygon') {
        const coordinatesText = document.getElementById('coordinates').value;
        const coordinatesPairs = coordinatesText.split(';').map(pair => {
            const [lat, lng] = pair.trim().split(',').map(Number);
            return [lng, lat];
        });
        coordinatesPairs.push(coordinatesPairs[0]); // Ensure polygon is closed
        geometry = {
            type: 'Polygon',
            coordinates: [coordinatesPairs]
        };
    }

    const submission = {
        type: 'Feature',
        geometry: geometry,
        properties: {
            name: document.getElementById('name').value,
            description: document.getElementById('description').value
        }
    };

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(submission)
    })
    .then(response => response.json())
    .then(data => {
        alert('Submission successful!');
        console.log(data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
