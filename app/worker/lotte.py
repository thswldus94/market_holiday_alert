import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re


class LotteManager:
    TYPE_CD = 'BC0701'

    def __init__(self, base_url):
        self.market_name = None
        self.base_url = base_url

        today = datetime.today()
        self.year = today.year
        self.month = today.month

    def get_holiday(self):
        try:
            response = requests.get(self.base_url, params={
                'schBrnchTypeCd': self.TYPE_CD,
                'schBrnchNm': self.market_name
            })

            # print(response)

            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')
                # print(soup)

                data = []
                branch_list = soup.find_all("div", class_='bx_type1')
                for branch in branch_list:
                    article = branch.find_all(class_=re.compile("article"))

                    name = article[0].find("h3").get_text()
                    holi = article[1].find("ul").get_text()
                    holi = holi.replace("\t", "")

                    data.append(f"name: {name}, holi: {holi}")

                return data
            else:
                print(response.status_code)
        except Exception as e:
            print(e)


