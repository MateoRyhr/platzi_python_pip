import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    # r_status = r.status_code
    print(r.status_code) # Estado de respuesta
    print(r.text)
    print(type(r.text)) # str --> needs to be converted to list
    categories = r.json() # parsing data in str to json or list of dict in python
    for category in categories:
        print(category['name'])