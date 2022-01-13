import os
from dotenv import load_dotenv
import long_polling


def main():
    load_dotenv()
    dvmn_token = os.getenv('dvmn_token')
    tg_token = os.getenv('tg_token')
    chat_id = os.getenv('chat_id')
    url = 'https://dvmn.org/api/long_polling/'
    long_polling.get_server_response(
        url, dvmn_token, tg_token, chat_id, timestamp=None
    )


if __name__ == "__main__":
    main()
