import os
from dotenv import load_dotenv
import long_polling
import telegram
import logging
from logging_tg_handler import TelegramBotHandler

bot_logger = logging.getLogger('bot_logger')


def main():
    load_dotenv()
    dvmn_token = os.getenv('DVMN_TOKEN')
    tg_token = os.getenv('TG_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')
    url = 'https://dvmn.org/api/long_polling/'
    bot = telegram.Bot(token=tg_token)
    bot_logger.setLevel(logging.DEBUG)
    bot_logger.addHandler(TelegramBotHandler(bot, tg_chat_id))
    long_polling.make_server_polling(
        url, dvmn_token, tg_chat_id, bot, timestamp=None)


if __name__ == "__main__":
    main()
