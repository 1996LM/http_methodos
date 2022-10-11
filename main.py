from urllib import response
import requests as rq
#para hacer una solicitud necesitamos la url
url = 'https://www.google.com/'
#vamos a crear un afuncion que de la libreria reques urilice get y como parametro tome la url y retorne el response
def get_requests(url):
    response=rq.get(url)
    return response

response = get_requests(url)
print(response.text)
