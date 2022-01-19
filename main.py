import os
from dotenv import load_dotenv
import long_polling
import telegram


def main():
    load_dotenv()
    dvmn_token = os.getenv('dvmn_token')
    tg_token = os.getenv('tg_token')
    chat_id = os.getenv('chat_id')
    url = 'https://dvmn.org/api/long_polling/'
    bot = telegram.Bot(token=tg_token)
    long_polling.make_server_polling(
        url, dvmn_token, chat_id, bot, timestamp=None)


if __name__ == "__main__":
    main()
