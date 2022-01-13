import telegram


def bot_sending_messages(token, chat_id, response):
    bot = telegram.Bot(token=token)
    bot.send_message(text='Работа вернулась с проверки', chat_id=chat_id)
    for attempt in response['new_attempts']:
        if attempt['is_negative']:
            bot.send_message(
                text=f'Задача \"{attempt["lesson_title"]}\" проверена, но есть '
                     f'ошибки. Подробнее: {attempt["lesson_url"]}',
                chat_id=chat_id
            )
        else:
            bot.send_message(
                text=f'Задача \"{attempt["lesson_title"]}\" '
                     f'проверена, все отлично!',
                chat_id=chat_id
            )

