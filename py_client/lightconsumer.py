import requests

endpoint = "http://127.0.0.1:8000/api/"

responSe = requests.post(endpoint, json={"title": "Hello World", "content": "Intoduction to Science", "price": "100"})

js_ = responSe.json()
print(js_)