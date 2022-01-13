import telegram


def bot_sending_messages(token, response):
    bot = telegram.Bot(token=token)
    bot.send_message(text='Работа вернулась с проверки', chat_id=210944506)
    for attempt in response['new_attempts']:
        if attempt['is_negative']:
            bot.send_message(
                text=f'Работа {attempt["lesson_title"]} проверена, но есть '
                     f'ошибки. Подробнее: {attempt["lesson_url"]}',
                chat_id=210944506
            )
        else:
            bot.send_message(
                text=f'Работа {attempt["lesson_title"]} проверена, все отлично!',
                chat_id=210944506
            )

