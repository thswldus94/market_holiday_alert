import os
import sys
from tools.common_util import DotDict
from tools.config_parser import load_config_from_section

from datetime import datetime
from app.action.telegram import Telegram

# config
config = DotDict()

# global path
g_path = os.path.abspath(os.path.dirname(sys.argv[0]))


def init_config():
    config_file = './config/config.ini'

    try:
        load_config_from_section(config_file, 'URLS', config)

    except Exception as e:
        print(e)
        sys.exit()


def run_service(market_type, market_name):
    # from app.worker.emart import EmartManager
    # from app.worker.lotte import LotteManager
    # from app.worker.homeplus import HomeplusManager

    from app.worker.manager import Manager

    manager = Manager(config)

    # manager.market_name = market_name

    manager.get_holiday()











