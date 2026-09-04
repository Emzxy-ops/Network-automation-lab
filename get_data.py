import requests

# 1. Define the target URL (The same endpoint we used in the REST Client)
url = "https://jsonplaceholder.typicode.com/todos/1"

# 2. Send the GET request
response = requests.get(url)

# 3. Print the results to the terminal so we can see them
print(f"Status Code: {response.status_code}")
print("\nResponse Data:")
print(response.json())