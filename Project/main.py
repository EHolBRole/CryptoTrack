import GUI.gui as gui
import API.api as api
import CRPC.crypto_proc as crypto_pr
import crypto as cr
from enums import Returns
from enums import Crypto


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
        btc = cr.coin
        raw_data = api.get_course(btc)

        parsed_data = crypto_pr.parse_data_for_graphic(raw_data)

        gui.draw_graphic(parsed_data)
    elif u_input == Returns.SHOW_CRYPTO_COURSE_TABLE:
        print("Drawing Table")
    elif u_input == Returns.SHOW_SETTINGS:
        print("Drawing Settings")
    elif u_input == Returns.SELECT_BTC:
        cr.change_coin_type(Crypto.BTC)
    elif u_input == Returns.SELECT_ETH:
        cr.change_coin_type(Crypto.ETH)
    elif u_input == Returns.SELECT_DOGE:
        cr.change_coin_type(Crypto.DOGE)
    elif u_input == Returns.SELECT_USDT:
        cr.change_coin_type(Crypto.USDT)

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
