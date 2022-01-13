import requests
import telegram_bot


def make_server_request(url, dvmn_token, timestamp):
    headers = {
        'Authorization': f'Token {dvmn_token}'
    }
    payload = {
        'timestamp': timestamp
    }
    response = requests.get(url, headers=headers, params=payload)
    print(response.json())
    return response.json()


def get_server_response(url, dvmn_token, tg_token, chat_id, timestamp):
    while True:
        try:
            response = make_server_request(url, dvmn_token, timestamp)
            if response['status'] == 'found':
                telegram_bot.bot_sending_messages(tg_token, chat_id, response)
                timestamp = response['last_attempt_timestamp']
            elif response['status'] == 'timeout':
                timestamp = response['timestamp_to_request']
        except requests.exceptions.ReadTimeout:
            response = make_server_request(url, dvmn_token, timestamp)
        except requests.exceptions.ConnectionError:
            pass

