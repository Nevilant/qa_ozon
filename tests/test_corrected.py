import random

import pytest

from pages.dog_page import DogAPI
from pages.ya_page import YaUploader


@pytest.mark.parametrize(
    'breed, path',
    [
        ('doberman', 'test_folder'),
        (random.choice(['bulldog', 'collie']), 'test_folder')
    ]
)
def test_check_upload_dog(breed, path, pre_condition):
    breed, path = pre_condition
    yandex_client = YaUploader()

    response = yandex_client.get_files_from_yd(path)

    # проверяем, что создалась папка
    assert response.json()['type'] == "dir"
    assert response.json()['name'] == "test_folder"

    # проверяем наличие файлов
    if not DogAPI().get_sub_breeds(breed):
        items = response.json()['_embedded']['items']
        assert len(items) == 1

        for item in items:
            assert item['type'] == 'file'
            print(f"Breed: {item['name']}")
            assert item['name'].startswith(breed), f"File name {item['name']} does not start with {breed}"

    else:
        items = response.json()['_embedded']['items']
        assert len(items) == len(DogAPI().get_sub_breeds(breed))
        for item in response.json()['_embedded']['items']:
            assert item['type'] == 'file'
            assert item['name'].startswith(breed), f"File name {item['name']} does not start with {breed}"

