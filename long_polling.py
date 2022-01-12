import requests


def get_reviews(url, token):
    headers = {
        'Authorization': f'Token {token}'
    }
    while True:
        try:
            response = requests.get(url, headers=headers)
            print(response.json())
            timestamp = response.json()['timestamp_to_request']
            payload = {
                'timestamp': timestamp
            }
            response = requests.get(url, headers=headers, params=payload)
            print(response.json())
        except requests.exceptions.ReadTimeout:
            response = requests.get(url, headers=headers)
        except requests.exceptions.ConnectionError:
            pass
    return response