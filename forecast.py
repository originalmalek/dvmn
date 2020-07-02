import requests

cities = ['лондон', 'шереметьево', 'череповец']

payload = {'nTq': '', 'lang': 'ru'}

for city in cities:
    url = 'http://wttr.in/' + city
    r = requests.get(url, params=payload)
    print(r.url)
    if r.ok:
        print(r.text)
    else:
        r.raise_for_status()
