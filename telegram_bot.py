import textwrap


def bot_sending_messages(bot, chat_id, response):
    bot.send_message(text='Работа вернулась с проверки', chat_id=chat_id)
    for attempt in response['new_attempts']:
        if attempt['is_negative']:
            text = f'''\
            Задача "{attempt['lesson_title']}" проверена, но есть ошибки.
            Подробнее: {attempt['lesson_url']}'''
            bot.send_message(text=textwrap.dedent(text), chat_id=chat_id)
        else:
            text = f'''\
            Задача "{attempt['lesson_title']}" проверена, все отлично!'''
            bot.send_message(text=textwrap.dedent(text), chat_id=chat_id)
