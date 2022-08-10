import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str, file_path_on_yadisc: str, overwrite=True):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }
        params = {
            "path": f"{file_path_on_yadisc}",
            "overwrite": f"{overwrite}"
        }
        response = requests.get(url=url, headers=headers, params=params).json()
        url2 = response["href"]

        with open(file_path, 'rb') as f:
            try:
                response = requests.put(url=url2, files={'file': f})
            except KeyError:
                print(response)
        return response.status_code


if __name__ == '__main__':
    path_to_local_file = ""
    file_path_on_yadisc = ""
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_local_file, file_path_on_yadisc)
    pprint(result)
