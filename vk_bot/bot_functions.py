import requests
import markovify

from conf import MODEL_PATH


def load_mark_model():
    model = markovify.Text.from_json(open(MODEL_PATH).read())
    return model


def get_dog_image():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    image = requests.get(url, stream=True, timeout=2)
    return image


def get_cat_image():
    contents = requests.get('https://aws.random.cat/meow').json()
    url = contents['file']
    image = requests.get(url, stream=True, timeout=2)
    return image


def upload_image(upload, image):
    photo = upload.photo_messages(photos=image.raw)[0]
    return f"photo{photo['owner_id']}_{photo['id']}"
