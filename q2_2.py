import requests
import json
from pprint import pprint


def upload(token: str, path: str):
    url = "https://cloud-api.yandex.net/v1/disk/resources/publish"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"OAuth {token}"
        }
    params = {"path": f"{path}"}
    response = requests.put(url=url, headers=headers, params=params)
    return response.json()


if __name__ == '__main__':
    token = ""
    path = ""
    pprint(upload(token, path))
