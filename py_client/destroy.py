import requests

endpoint = "http://127.0.0.1:8000/api/products/"

product_id = input("please input the product id you wish to delete: ")

try:
    product_id = int(product_id)
    id_string = f"{product_id}/delete"
    new_endpoint = endpoint + id_string
    response = requests.delete(new_endpoint)
    delete_response = response.json()
    print('Item Successfully deleted')
except:
    print('Invalid product id')





