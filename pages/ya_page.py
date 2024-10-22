import os

import requests
from dotenv import load_dotenv

load_dotenv()


class YaUploader:
    base_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    token = os.getenv('YANDEX_OAUTH_TOKEN')
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'OAuth {token}'
    }

    def create_folder(self, path):
        """
        Создаем каталог
        :param path: название каталога
        :return: возвращаем response
        """
        response = requests.put(
            f'{self.base_url}?path={path}',
            headers=self.headers)
        return response

    def upload_photos_to_yd(self, path, url_file, name):
        """
        Загружаем фотографию в каталог
        :param path: название каталога
        :param url_file: передаем URL файла,
        :param name: передаем имя файла
        :return:
        """
        url = f'{self.base_url}/upload'
        params = {
            "path": f'/{path}/{name}',
            'url': url_file,
            "overwrite": "true"
        }
        response = requests.post(
            url=url,
            headers=self.headers,
            params=params
        )
        return response

    def get_files_from_yd(self, path):
        """
        Получаем информацию о файле или каталоге
        :param path: название каталога
        :return: возвращаем response
        """
        response = requests.get(
            url=f'{self.base_url}?path={path}',
            headers=self.headers
        )
        return response

    def delete_folder(self, path: str):
        """
        Удаляем каталог
        :param path: название каталога
        :return: возвращаем response
        """
        params = {
            "path": f'/{path}',
            "force_async": True,
            "permanently": True
        }
        response = requests.delete(
            url=self.base_url,
            headers=self.headers,
            params=params
        )
        return response
