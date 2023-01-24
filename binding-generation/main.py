import requests
import json




def fmt_url(name):
    return f'https://developer.apple.com/tutorials/data/documentation/metal/{name}.json'


def fmt_json(json_string):
    return json.loads(json_string)


def request(name):
    url = f'https://developer.apple.com/tutorials/data/documentation/metal/{name}.json'

    page = requests.get(url)

    return fmt_json(page.text)


print(request('mtltrianglefillmode'))