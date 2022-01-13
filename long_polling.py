import requests
import telegram_bot


def get_server_response(url, token, tg_token):
    headers = {
        'Authorization': f'Token {token}'
    }
    while True:
        try:
            response = requests.get(url, headers=headers)
            print(response.json())
            response = response.json()
            if response['status'] == 'found':
                telegram_bot.bot_sending_messages(tg_token, response)
                timestamp = response['last_attempt_timestamp']
                payload = {
                    'timestamp': timestamp
                }
                response = requests.get(url, headers=headers, params=payload)
            elif response['status'] == 'timeout':
                timestamp = response['timestamp_to_request']
                payload = {
                    'timestamp': timestamp
                }
                response = requests.get(url, headers=headers, params=payload)
        except requests.exceptions.ReadTimeout:
            response = requests.get(url, headers=headers)
        except requests.exceptions.ConnectionError:
            pass

