import requests

print(requests.get("http://httpbin.org/get").json())
