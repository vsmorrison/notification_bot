import logging


class TelegramBotHandler(logging.Handler):

    def __init__(self, tg_logging_bot, tg_chat_id):
        super().__init__()
        self.tg_chat_id = tg_chat_id
        self.tg_logging_bot = tg_logging_bot

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_logging_bot.send_message(
            chat_id=self.tg_chat_id, text=log_entry
        )


def make_bot_logger(bot, chat_id):
    bot_logger = logging.getLogger('bot_logger')
    bot_logger.setLevel(logging.DEBUG)
    bot_logger.addHandler(TelegramBotHandler(bot, chat_id))
    return bot_logger
