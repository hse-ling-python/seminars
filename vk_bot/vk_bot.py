import random

from vk_api import VkUpload, VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from conf import TOKEN, GROUP_ID
from bot_functions import get_cat_image, get_dog_image, upload_image, load_mark_model

vk_session = VkApi(token=TOKEN)
long_poll = VkBotLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()
upload = VkUpload(vk_session)
tolstoy = load_mark_model()


def send_pet(event, kind="cat"):
    vk.messages.send(
        user_id=event.obj.from_id, random_id=random.getrandbits(50),
        message='секундочку...'
    )
    if kind == 'cat':
        image = get_cat_image()
    else:
        image = get_dog_image()
    photo = upload_image(upload, image)
    vk.messages.send(
        user_id=event.obj.from_id, random_id=random.getrandbits(50),
        message='...', attachment=photo
    )


def send_tolstoy(event):
    text = tolstoy.make_short_sentence(280)
    vk.messages.send(
        user_id=event.obj.from_id, random_id=random.getrandbits(50),
        message=text
    )


def handle_new_message(event):
    if 'DOG' in event.obj.text:
        send_pet(event, kind='dog')
    elif 'CAT' in event.obj.text:
        send_pet(event, kind='cat')
    else:
        send_tolstoy(event)


def new_message_timeout_error(event):
    vk.messages.send(
        user_id=event.obj.from_id, random_id=random.getrandbits(50),
        message="у меня интернет не очень и не успеваю качать картинки : ("
    )


def new_message_error(event):
    vk.messages.send(
        user_id=event.obj.from_id, random_id=random.getrandbits(50),
        message="у меня что-то сломалось, давайте еще раз попробуем"
    )


def main():
    for event in long_poll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            try:
                handle_new_message(event)
            except TimeoutError:
                new_message_timeout_error(event)
            except:
                new_message_error(event)


if __name__ == '__main__':
    main()
