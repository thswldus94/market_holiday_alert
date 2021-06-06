import requests
from datetime import datetime


class HomeplusManager:
    def __init__(self, base_url):
        self.market_name = None
        self.base_url = base_url

        today = datetime.today()
        self.year = today.year
        self.month = today.month

    def get_holiday(self):
        try:
            response = requests.post(self.base_url, data={
                'areaCd': self.AREA_CD,
                'year': self.year,
                'month': self.month,
                'keyword': self.market_name
            })

            print(response)
        except Exception as e:
            print(e)


