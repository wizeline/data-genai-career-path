import http
from uuid import uuid4

import requests


def store_image(image_url: str) -> str:
    response = requests.get(image_url)

    if response.status_code != http.HTTPStatus.OK:
        raise Exception('There is an error downloading the image')

    content = response.content

    random_uuid = uuid4()
    local_image_path = f'tmp/{random_uuid}.png'

    with open(local_image_path, 'wb') as file:
        file.write(content)

    return local_image_path
