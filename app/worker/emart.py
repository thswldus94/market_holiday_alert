#-*- coding:utf-8 -*-

import requests
from datetime import datetime
# from app.action.telegram import Telegram


class EmartManager:
    JMODE = 'true'

    def __init__(self, base_url):
        self.market_name = None
        self.base_url = base_url

        today = datetime.today()
        self.year = today.year
        self.month = '{:02d}'.format(today.month)

    def get_holiday(self):
        try:
            # print({
            #     'jMode': self.JMODE,
            #     'year': self.year,
            #     'month': self.month,
            #     'keyword': self.market_name
            # })
            # print(self.base_url)
            response = requests.post(self.base_url, data={
                'jMode': self.JMODE,
                'year': self.year,
                'month': self.month,
                'keyword': self.market_name
            })
            res_json = response.json()
            result = res_json['dataList']
            print(result)

            data = []
            for res in result:
                # data.append({
                #     'name': res['NAME'],
                #     'holiday1': res['HOLIDAY_DAY1_YYYYMMDD'],
                #     'holiday2': res['HOLIDAY_DAY2_YYYYMMDD'],
                #     'holiday3': res['HOLIDAY_DAY3_YYYYMMDD']
                # })

                data.append(f"name: {res['NAME']}, holi1: {res['HOLIDAY_DAY1_YYYYMMDD']}, holi2: {res['HOLIDAY_DAY2_YYYYMMDD']}, holi2: {res['HOLIDAY_DAY3_YYYYMMDD']}")

            print(data)

            return data
        except Exception as e:
            print(e)

