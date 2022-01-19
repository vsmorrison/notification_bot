import requests
import telegram_bot
import time


def get_server_response(url, dvmn_token, timestamp):
    headers = {
        'Authorization': f'Token {dvmn_token}'
    }
    payload = {
        'timestamp': timestamp
    }
    response = requests.get(url, headers=headers, params=payload)
    return response.json()


def make_server_polling(url, dvmn_token, chat_id, bot, timestamp):
    connection_error_counter = 0
    while True:
        try:
            server_response = get_server_response(url, dvmn_token, timestamp)
            if server_response['status'] == 'found':
                telegram_bot.bot_sending_messages(
                    bot, chat_id, server_response
                )
                timestamp = server_response['last_attempt_timestamp']
            elif server_response['status'] == 'timeout':
                timestamp = server_response['timestamp_to_request']
        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            connection_error_counter += 1
            if not connection_error_counter % 10:
                time.sleep(60)
                connection_error_counter = 0

