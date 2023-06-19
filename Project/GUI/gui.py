import PySimpleGUI as psg
import matplotlib.pyplot as plt

from enums import Returns


crypto_course_graph = psg.Graph(canvas_size=(255, 255),
                                graph_top_right=(600, 200),
                                graph_bottom_left=(150, 0),
                                background_color='white')


def draw_graphic(p_data):

    pass


def gui_processing(to_close=False):
    u_input = Returns.NULL  # should be ENUM

    if to_close:
        window.close()
        return Returns.EXIT

    event, values = window.read()
    print(event, values)

    if event in (None, 'Exit'):
        return Returns.EXIT
    elif event in (None, "Show Graphic"):
        return Returns.SHOW_CRYPTO_COURSE_GRAPH
    elif event in (None, "Show Table"):
        return Returns.SHOW_CRYPTO_COURSE_TABLE
    elif event in (None, "Settings"):
        return Returns.SHOW_SETTINGS
    elif event in (None, "Bitcoin"):
        return Returns.SELECT_BTC
    elif event in (None, "Etherium"):
        return Returns.SELECT_ETH
    elif event in (None, "Dogecoin"):
        return Returns.SELECT_DOGE
    elif event in (None, "USDT"):
        return Returns.SELECT_USDT

    return u_input


def get_crypto_col():
    button_bitcoin = psg.Button("Bitcoin")
    button_dogecoin = psg.Button("Dogecoin")
    button_etherium = psg.Button("Etherium")
    button_usdt = psg.Button("USDT")

    layout_for_col = [[button_bitcoin, button_dogecoin, button_etherium, button_usdt]]

    return psg.Column(layout_for_col, expand_x=True)


def get_options_col():
    button_exit = psg.Exit("Exit")
    button_show_graph = psg.Button("Show Graphic")
    button_show_table = psg.Button("Show Table")
    button_settings = psg.Button("Settings")

    layout_for_col = [[button_exit],
                      [button_show_graph],
                      [button_show_table],
                      [button_settings]
                      ]

    return psg.Column(layout_for_col, expand_y=True)


def get_layout():

    col_options = get_options_col()
    col_crypto = get_crypto_col()

    course_graph = crypto_course_graph

    layout = [
        [course_graph, col_options],
        [col_crypto]
    ]

    return layout


psg.theme('DarkAmber')

window = psg.Window('CryptoTrack', get_layout())
