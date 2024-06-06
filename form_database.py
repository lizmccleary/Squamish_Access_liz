import requests 
import json 
import base64

def save_to_github(description, observation_time, location_coordinates, notes, picture_data, github_token):
    # Define repository information
    repo_owner = 'lizmccleary'
    repo_name = 'Squamish_Access_liz'
    file_path = '/Users/lizmccleary/Documents/GitHub/Squamish_Access_liz/form_data.txt'

    # Format data to be saved 
    data = {
        'description': description, 
        'observation_time': observation_time, 
        'location_coordinates': location_coordinates, 
        'notes': notes, 
        'picture_data': picture_data
    }

    # Convert data to JSON 
    json_data = json.dumps(data)

    # Prepare headers for API request 
    headers = {
        'Authorization': f'token {github_token}', 
        'Accept': 'application/vnd.github.v3+json'
    }

    # Retrieve existing file content 
    response = requests.get(f'https://api.github.com/repos/{lizmccleary}/{Squamish_Access_liz}/contents/{/Users/lizmccleary/Documents/Github/Squamish_Access_liz/form_data.txt}', 
                            headers=headers)
    
    if response.status_code ==200: 
        existing_content = response.json()
        current_content = base64.b64decode(existing_content['content']).decode()
    else: 
        current_content = '[]' # If the file doesn't exist, start w empty list 

    # Append new submission to existing content 
    submissions = json.loads(current_content)
    submissions.append(data)
    updated_content = json.dumps(submissions)

    # Update file in the repository 
    response = requests.put(f'https://api.github.com/repos/{lizmccleary}/{Squamish_Access_liz}/contents/{/Users/lizmccleary/Documents/GitHub/Squamish_Access_liz/form_data.txt}', 
                            headers=headers, 
                            json={
                                'message': 'Add new form submission', 
                                'content': base64.b64encode(json_data.encode()).decode(), 
                                'branch': 'main', 
                                'sha': existing_content.get('sha', None) # Include SHA for updating existing file 
                            })
    
    if response.status_code == 200:
        print('Form data saved successfully to GitHub.')
    else:
        print(f'Error: {response.status_code}')
