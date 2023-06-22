import PySimpleGUI as psg
import matplotlib.pyplot as plt

from enums import Returns

from API.hol_api import ParsedData


GRAPH_CORDS = [(-20, -15), (256, 256)]


def draw_graphic(p_data: ParsedData, window: psg.Window):
    window['-GRAPH-'].erase()
    last_x = 0
    last_y = p_data.values[0] / (p_data.max_value / (GRAPH_CORDS[1][1] - 10))
    for i in range(1, 13):
        window['-GRAPH-'].draw_text(f'{int(p_data.max_value / 12) * i}', (-10, ((GRAPH_CORDS[1][1]-10)/12)*i), color='black', font=None, angle=0)
        window['-GRAPH-'].DrawLine((0, ((GRAPH_CORDS[1][1]-10)/12)*i), (GRAPH_CORDS[1][0], ((GRAPH_CORDS[1][1]-10)/12)*i), width=1, color="LIGHT GRAY")
    window['-GRAPH-'].DrawLine((0, 0), (0, GRAPH_CORDS[1][1]), width=1, color="BLACK")
    window['-GRAPH-'].DrawLine((0, 0), (GRAPH_CORDS[1][0], 0), width=1, color="BLACK")
    window['-GRAPH-'].draw_text(f'{p_data.dates[0]}', (0, -10), color='black', font=None, angle=0)
    counter_x = 0
    for index in range(1, p_data.format):
        print(p_data.dates[index], p_data.values[index])
        counter_x += 1
        x = ((GRAPH_CORDS[1][0]-5)/p_data.format) * counter_x
        y = p_data.values[index] / (p_data.max_value / (GRAPH_CORDS[1][1] - 10))
        window['-GRAPH-'].draw_text(f'{p_data.dates[index]}', (x, -10), color='black', font=None, angle=0)
        window['-GRAPH-'].DrawLine((x, -5), (x, y), width=1, color="GREEN")
        window['-GRAPH-'].DrawLine((last_x, last_y), (x, y), width=1, color="BLACK")
        last_x = ((GRAPH_CORDS[1][0]-5)/p_data.format) * counter_x
        last_y = p_data.values[index] / (p_data.max_value / (GRAPH_CORDS[1][1] - 10))
    return True


def gui_processing(to_close=False):
    u_input = Returns.NULL

    if to_close:
        main_window.close()
        return Returns.EXIT

    event, values = main_window.read()
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
    elif event in (None, "Binance Coin"):
        return Returns.SELECT_BNB
    elif event in (None, "Yearn.Finance"):
        return Returns.SELECT_YFI

    return u_input


def get_crypto_col():
    button_bitcoin = psg.Button("Bitcoin")
    button_etherium = psg.Button("Etherium")
    button_binance_coin = psg.Button("Binance Coin")
    button_waltonchain = psg.Button("Yearn.Finance")

    layout_for_col = [[button_bitcoin, button_etherium, button_binance_coin, button_waltonchain]]

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
    crypto_course_graph = psg.Graph(canvas_size=(1024, 740),
                                    graph_top_right=(GRAPH_CORDS[1]),
                                    graph_bottom_left=(GRAPH_CORDS[0]),
                                    background_color='yellow', key="-GRAPH-")

    col_options = get_options_col()
    col_crypto = get_crypto_col()

    course_graph = crypto_course_graph

    layout = [
        [course_graph, col_options],
        [col_crypto]
    ]

    return layout


psg.theme('DarkAmber')

main_window = psg.Window('CryptoTrack', get_layout())
