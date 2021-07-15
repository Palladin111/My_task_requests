import requests


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.token = ' '

    # Избавляемся от эскейп последовательностей в пути к файлу
    def get_path_right(self):
        list = []

        # Определяем список кодов ескейп последовательностей и список кодов символов
        list_1 = [[7, 8, 12, 10, 13, 9, 11], [97, 98, 102, 110, 114, 116, 118]]

        for char in self.file_path:
            char = ord(char)
            for char_1 in list_1[0]:
                if char == char_1:
                    char_2 = char
                    char = 47
                    list.append(char)
                    char = list_1[1][list_1[0].index(char_2)]
            list.append(char)

        list_2 = []

        for byte in list:
            byte = chr(byte)
            list_2.append(byte)
        file_path_1 = "".join(list_2)
        return file_path_1

    def get_file_name(self):
        list_name = []
        for name in self.get_path_right().split('/'):
            list_name.append(name)
        file_name = list_name[-1]
        return file_name

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": self.get_file_name(), "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self):
        href = self.get_upload_link().get("href", "")
        response = requests.put(href, data=open(self.get_path_right(), 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            ok = "Файл успешно загружен"
        return print(ok)


if __name__ == '__main__':
    uploader = YaUploader('C:\files_1\files.txt')
    result = uploader.upload()