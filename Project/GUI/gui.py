import PySimpleGUI as psg
import matplotlib.pyplot as plt

from enums import Returns


def draw_graphic(p_data: [int, int], window: psg.Window):
    window['-GRAPH-'].erase()
    last_x = 0
    last_y = 0
    window['-GRAPH-'].draw_text('0', (-10, 0), color='black', font=None, angle=0)
    window['-GRAPH-'].draw_text('25', (-10, 25), color='black', font=None, angle=0)
    window['-GRAPH-'].draw_text('50', (-10, 50), color='black', font=None, angle=0)
    window['-GRAPH-'].draw_text('75', (-10, 75), color='black', font=None, angle=0)
    window['-GRAPH-'].draw_text('90', (-10, 90), color='black', font=None, angle=0)
    window['-GRAPH-'].draw_text('105', (-10, 105), color='black', font=None, angle=0)
    window['-GRAPH-'].draw_text('120', (-10, 130), color='black', font=None, angle=0)
    for dot in p_data:
        print(dot[0], dot[1])
        x = dot[0]
        y = dot[1]
        window['-GRAPH-'].draw_text(f'{x}', (x, -10), color='black', font=None, angle=0)
        window['-GRAPH-'].DrawLine((last_x, last_y), (x, y), width=1, color="BLACK")
        last_x = dot[0]
        last_y = dot[1]
    while last_x < 130:
        last_x += 15
        window['-GRAPH-'].draw_text(f'{last_x}', (last_x, -10), color='black', font=None, angle=0)
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
    crypto_course_graph = psg.Graph(canvas_size=(255, 255),
                                    graph_top_right=(140, 140),
                                    graph_bottom_left=(-20, -15),
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
