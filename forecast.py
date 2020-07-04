import requests


def get_weather(places):

    payload = {'nTq': '', 'lang': 'ru'}

    for place in places:
        url = 'http://wttr.in/' + place
        response = requests.get(url, params=payload)
        if response.ok:
            print(response.text)
        else:
            print('Response error' + response.status_code)


def main():
    places = ('лондон', 'шереметьево', 'череповец')
    get_weather(places)


if __name__ == '__main__':
    main()
