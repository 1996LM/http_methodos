from urllib import response
import requests as rq
url='http://httpbin.org/'

def get_requests(url):
    response = rq.get(url+'get') #'get' asi lo pide la url
    return response.json()

def post_requests(url):
    response = rq.post(url+'post')
    return response.json()

response = post_requests(url)
print(response)

