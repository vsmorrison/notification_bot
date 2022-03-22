import os
from dotenv import load_dotenv
import long_polling
import telegram
import logging_tools


def main():
    load_dotenv()
    dvmn_token = os.getenv('DVMN_TOKEN')
    tg_token = os.getenv('TG_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')
    url = 'https://dvmn.org/api/long_polling/'
    bot = telegram.Bot(token=tg_token)
    logger = logging_tools.make_bot_logger(bot, tg_chat_id)
    long_polling.make_server_polling(
        url, dvmn_token, tg_chat_id, bot, logger, timestamp=None)


if __name__ == "__main__":
    main()
