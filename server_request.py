import requests
url = 'http://localhost:5000/api'

print('ready')
while True:
    text = input()
    r = requests.post(url,json={'text':text,})
    print(r.json())