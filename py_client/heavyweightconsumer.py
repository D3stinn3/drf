import requests

endpoint = 'http://127.0.0.1:8000/api/products/'
"""data = {
    "title": "Hello Mary",
    "content": "Mary is Here"
}"""
response = requests.get(endpoint)
print(response.json())