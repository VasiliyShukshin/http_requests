import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources/publish"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }
        params = {"path": f"{file_path}"}
        response = requests.put(url=url, headers=headers, params=params)
        print(response.status_code)
        return response.json()


if __name__ == '__main__':
    path_to_file = ""
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    pprint(result)
