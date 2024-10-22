import requests


class DogAPI:
    base_url = 'https://dog.ceo/api/breed'

    def get_sub_breeds(self, breed):
        """
        Получаем список подпород
        :param breed: указываем породу
        :return: возвращает список пород
        """
        response = requests.get(f'{self.base_url}/{breed}/list')
        return response.json().get('message', [])

    def get_urls_img(self, breed, sub_breeds):
        """
        Получаем список URL картинок пород, либо подпород
        :param breed: указываем породу
        :param sub_breeds: указываем подпороду
        :return: получаем список URL картинок пород, либо подпород
        """
        url_images = []
        if sub_breeds:
            for sub_breed in sub_breeds:
                response = requests.get(
                    url=f"{self.base_url}/{breed}/{sub_breed}/images/random"
                )
                sub_breed_urls = response.json().get('message')
                url_images.append(sub_breed_urls)
        else:
            response = requests.get(
                url=f"{self.base_url}/{breed}/images/random"
            )
            breed_url = response.json().get('message')
            url_images.append(breed_url)
        return url_images
