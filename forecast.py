import requests


def print_weather(places :list):
    """
    :param places:
    :return: None, if error
    """

    payload = {'nTq': '', 'lang': 'ru'}

    for place in places:
        url = 'http://wttr.in/' + place
        response = requests.get(url, params=payload)
        if response.ok:
            print(response.text)
        else:
            return


def main():
    places = ['лондон', 'шереметьево', 'череповец']
    print_weather(places)


if __name__ == '__main__':
    main()
