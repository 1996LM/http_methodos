from tkinter import E
import requests as rq
url = 'https://pokeapi.co/api/v2/pokemon/ditto'

def get_requests(url):
    try:
        response = rq.get(url)
        return response
    except Exception as e:
        raise e 


response = get_requests(url)
print(response.json())
