import GUI.gui as gui
import API.api as api
import CRPC.crypto_proc as crypto_pr
import crypto_control as cr
import crypto as crypt
import API.hol_api as hol_api
import enums
import json

from enums import Returns
from enums import Crypto

coin = crypt.CryptoCurrency()


def init():
    pass


def close_all():
    gui.gui_processing(True)
    pass


def parse_input(u_input):
    global coin
    if u_input == Returns.EXIT:
        return False
    elif u_input == Returns.SHOW_CRYPTO_COURSE_GRAPH:
        print("Drawing Graphic")
        Binance = api.BinanceAPI()
        # raw_data = Binance.getHistoryData(coin).content
        # parsed_data = crypto_pr.parse_data_for_graphic(raw_data)
        hol_binance = hol_api.HOL_API()
        parsed_data = hol_binance.GetHistoricalData(gui.SETTINGS['HOWLONG'], coin.type, gui.SETTINGS['INTCOMBO'])
        print(parsed_data)
        gui.draw_graphic(parsed_data, gui.main_window, coin.type)
    elif u_input == Returns.SHOW_CRYPTO_COURSE_CURRENT:
        print("Drawing Current Course")
        Binance = api.BinanceAPI()
        is_again = False
        while not is_again:
            parsed_data = []
            for en in enums.Crypto:
                coin = cr.change_coin_type(en)
                raw_data = Binance.get_course(coin).content
                parsed_data.append(json.loads(raw_data))
            is_again = gui.draw_current_course(parsed_data, gui.main_window, coin.type)
    elif u_input == Returns.SHOW_SETTINGS:
        gui.draw_settings()
        print("Drawing Settings")
    elif u_input == Returns.SELECT_BTC:
        coin = cr.change_coin_type(Crypto.BTC)
    elif u_input == Returns.SELECT_ETH:
        coin = cr.change_coin_type(Crypto.ETH)
    elif u_input == Returns.SELECT_BNB:
        coin = cr.change_coin_type(Crypto.BNB)
    elif u_input == Returns.SELECT_YFI:
        coin = cr.change_coin_type(Crypto.YFI)

    return True


def main():
    init()
    is_running = True
    while is_running:
        user_input = gui.gui_processing()
        is_running = parse_input(user_input)
    close_all()
    pass


main()
print("Спасибо за внимание!")
