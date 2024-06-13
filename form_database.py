import requests
import json
import base64


def save_to_github(description, observation_time, location_coordinates, notes, picture_data, github_token):
   # Define repository information
   repo_owner = 'lizmccleary'
   repo_name = 'Squamish_Access_liz'
   file_path = 'form_data.txt'


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
   url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'
   response = requests.get(url, headers=headers)


   if response.status_code == 200:
       existing_content = response.json()
       current_content = base64.b64decode(existing_content['content']).decode()
       submissions = json.loads(current_content)
       sha = existing_content['sha']
   else:
       submissions = []
       sha = None


   # Append new submission to existing content
   submissions.append(data)
   updated_content = json.dumps(submissions)


   # Update file in the repository
   update_data = {
       'message': 'Add new form submission',
       'content': base64.b64encode(updated_content.encode()).decode(),
       'branch': 'main',
   }
   if sha:
       update_data['sha'] = sha


   response = requests.put(url, headers=headers, json=update_data)


   if response.status_code == 200:
       print('Form data saved successfully to GitHub.')
   else:
       print(f'Error: {response.status_code} {response.json()}')


# Example usage
save_to_github(
   description="Sample description",
   observation_time="2024-06-06T12:00:00Z",
   location_coordinates="49.2827,-123.1207",
   notes="Sample notes",
   picture_data="base64_encoded_image_data",
   github_token="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"
)
