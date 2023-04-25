import requests

endpoint = "http://127.0.0.1:8000/api/products/3/update"

data_to_be_appended = {
    "title": "Syria",
    "price": "200",
    "content": "Hello people"
}
responSe = requests.put(endpoint, json=data_to_be_appended)
data_ = responSe.json()
print(data_)


