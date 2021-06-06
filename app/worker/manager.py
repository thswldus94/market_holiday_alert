import requests
from datetime import datetime
from app.action.telegram import Telegram


class Manager:
    def __init__(self, config):
        self.tele = Telegram
        self.config = config

    def get_holiday(self):
        try:
            self.tele = Telegram(self.config)
            self.tele.get_message()
            while True:
                pass
        except Exception as e:
            print(e)

