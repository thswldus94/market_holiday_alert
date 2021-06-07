import telegram
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

from app.worker.emart import EmartManager
from app.worker.lotte import LotteManager
from app.worker.homeplus import HomeplusManager


class Telegram:
    TOKEN = '1801479266:AAGqJeNRu18LUP5Z6ASDQVWI35C9mCwbrB0'

    def __init__(self, config):
        print("telegram start")
        self.bot = telegram.Bot(token = self.TOKEN)
        self.updater = Updater(token=self.TOKEN, use_context=True)
        self.dispatcher = self.updater.dispatcher

        self.config = config

    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="아씨 마트 언제쉬냐?")

    def echo(self, update, context):
        user_id = update.effective_chat.id
        user_text = update.message.text

        split_list = user_text.split()
        if len(split_list) < 2:
            context.bot.send_message(chat_id=user_id, text="마트 번호와 지점명을 입력해주세요. ex) 1 분당")
            return False

        market_type = split_list[0]
        market_name = split_list[1]

        if market_type is None or market_name is None:
            context.bot.send_message(chat_id=user_id, text="마트 번호와 지점명을 입력해주세요. ex) 1 분당")
            return False

        if market_type == '1':
            manager = EmartManager(self.config.EMART_BASE_URL)
        elif market_type == '2':
            manager = LotteManager(self.config.LOTTE_BASE_URL)
        else:
            context.bot.send_message(chat_id=user_id, text="준비중입니다")

        manager.market_name = market_name
        result = manager.get_holiday()
        for res in result:
            context.bot.send_message(chat_id=user_id, text=res)

    def send_message(self, chat_id, text):
        self.bot.sendMessage(chat_id=chat_id, text=text)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

    def get_message(self):
        # start_handler = CommandHandler('start', self.start)
        # self.dispatcher.add_handler(start_handler)

        echo_handler = MessageHandler(Filters.text & (~Filters.command), self.echo)
        self.dispatcher.add_handler(echo_handler)

        self.updater.start_polling()






