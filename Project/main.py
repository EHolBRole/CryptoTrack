import GUI.gui as gui
import API.api as api
import CRPC.crypto_proc as crypto_pr
import crypto as cr


def init():
    pass


def close_all():
    pass


def parse_input(u_input):
    if u_input == "Show_Crypto_Course":
        btc = cr.CryptoCurrency()
        raw_data = api.get_course(btc)

        parsed_data = crypto_pr.parse_data_for_graphic(raw_data)

        gui.draw_graphic(parsed_data)
        return True
    pass


def main():
    init()
    is_running = True
    while is_running:
        user_input = gui.user_input()
        parse_input(user_input)
    close_all()
    pass


main()
print("Спасибо за внимание!")
