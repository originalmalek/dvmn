import requests


def main()
    cities = ['лондон', 'шереметьево', 'череповец']
    
    payload = {'nTq': '', 'lang': 'ru'}

    for city in cities:
        url = 'http://wttr.in/' + city
        r = requests.get(url, params=payload)
        if r.ok:
            print(r.text)
        else:
            print('Response error' + r.status_code)


if __name__ == '__main__':
    main()
