import requests
import telegram_bot
import time


def get_students_reviews(url, dvmn_token, timestamp):
    headers = {
        'Authorization': f'Token {dvmn_token}'
    }
    payload = {
        'timestamp': timestamp
    }
    response = requests.get(url, headers=headers, params=payload)
    return response.json()


def make_server_polling(url, dvmn_token, chat_id, bot, logger, timestamp):
    connection_error_counter = 0
    logger.info('Бот запущен')
    while True:
        try:
            students_reviews = get_students_reviews(url, dvmn_token, timestamp)
            if students_reviews['status'] == 'found':
                telegram_bot.bot_sending_messages(
                    bot, chat_id, students_reviews
                )
                timestamp = students_reviews['last_attempt_timestamp']
            elif students_reviews['status'] == 'timeout':
                timestamp = students_reviews['timestamp_to_request']
        except requests.exceptions.ReadTimeout:
            logger.warning('Сервер не отправил данные')
            pass
        except requests.exceptions.ConnectionError:
            logger.error('Проблемы с соединением')
            connection_error_counter += 1
            if not connection_error_counter % 10:
                time.sleep(60)
                connection_error_counter = 0

