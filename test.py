import json
import requests

# Define the JSON data to be sent
data = {'name': 'John Doe', 'age': 30}

# Convert the data to JSON format
json_data = json.dumps(data)

# Set the URL of the server
url = 'http://localhost:5000/data'

# Send the JSON data to the server using HTTP POST method
response = requests.post(url, json=json_data)

# Print the response status code
print('Response status code:', response.status_code)