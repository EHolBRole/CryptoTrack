import GUI.gui as gui
import API.api as api
import CRPC.crypto_proc as crypto_pr
import crypto_control as cr
import crypto as crypt
import API.hol_api as hol_api

from enums import Returns
from enums import Crypto

coin = crypt.CryptoCurrency()


def init():
    pass


def close_all():
    gui.gui_processing(True)
    pass


def parse_input(u_input):
    if u_input == Returns.EXIT:
        return False
    elif u_input == Returns.SHOW_CRYPTO_COURSE_GRAPH:
        print("Drawing Graphic")
        Binance = api.BinanceAPI()
        global coin
        # raw_data = Binance.getHistoryData(coin).content
        # parsed_data = crypto_pr.parse_data_for_graphic(raw_data)
        hol_binance = hol_api.HOL_API()
        parsed_data = hol_binance.GetHistoricalData(180, coin.type, '1w')
        print(parsed_data)
        gui.draw_graphic(parsed_data, gui.main_window, coin.type)
    elif u_input == Returns.SHOW_CRYPTO_COURSE_TABLE:
        print("Drawing Table")
    elif u_input == Returns.SHOW_SETTINGS:
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
