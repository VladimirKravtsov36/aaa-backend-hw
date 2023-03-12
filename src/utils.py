
import requests
import io
from requests.exceptions import ConnectionError
from PIL import UnidentifiedImageError

def recognize_text(url, id, reader):

    try:
        image = requests.get(f'{url}/{id}', timeout=5)
    except ConnectionError:
        return {'error': 'Image service is unavailable'}, 500

    image = io.BytesIO(image.content)

    try:
        text = reader.read_text(image)
    except UnidentifiedImageError:
        return {'error': 'invalid image'}, 400

    return {id: text}, 200