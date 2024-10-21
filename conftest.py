import pytest

from pages.dog_page import DogAPI
from pages.ya_page import YaUploader


@pytest.fixture()
def pre_condition(breed, path):
    sub_breeds = DogAPI().get_sub_breeds(breed=breed)
    urls = DogAPI().get_urls_img(breed=breed, sub_breeds=sub_breeds)
    yandex_client = YaUploader()
    yandex_client.create_folder(path)
    for url in urls:
        part_name = url.split('/')
        name = '_'.join([part_name[-2], part_name[-1]])
        yandex_client.upload_photos_to_yd(path, url, name)

    yield breed, path

    yandex_client.delete_folder(path)
    print("\nКаталог удален")
