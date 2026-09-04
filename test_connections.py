import requests
import json

# Using a standard public network / configuration endpoint
url = "https://jsonplaceholder.typicode.com/users/1"

# Execute the GET request (no special API key needed for this sandbox)
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Output results
print(f"Status Code: {response.status_code}")
print(f"Network Engineer Name: {data['name']}")
print(f"Company: {data['company']['name']}")