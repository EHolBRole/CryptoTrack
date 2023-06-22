import PySimpleGUI as psg
import matplotlib.pyplot as plt

from enums import Returns

from API.hol_api import ParsedData


GRAPH_CORDS = [(-20, -15), (256, 256)]

SETTINGS = {'INTCOMBO': '1w', 'HOWLONG': 30}


def draw_graphic(p_data: ParsedData, window: psg.Window, crypto_type):
    window['-GRAPH-'].erase()
    last_x = 0
    last_y = p_data.values[0] / (p_data.max_value / (GRAPH_CORDS[1][1] - 10))
    for i in range(1, 13):
        window['-GRAPH-'].draw_text(f'{int(p_data.max_value / 12) * i}', (-10, ((GRAPH_CORDS[1][1]-10)/12)*i), color='black', font=None, angle=0)
        window['-GRAPH-'].DrawLine((0, ((GRAPH_CORDS[1][1]-10)/12)*i), (GRAPH_CORDS[1][0], ((GRAPH_CORDS[1][1]-10)/12)*i), width=1, color="LIGHT GRAY")
    window['-GRAPH-'].DrawLine((0, 0), (0, GRAPH_CORDS[1][1]), width=1, color="BLACK")
    window['-GRAPH-'].DrawLine((0, 0), (GRAPH_CORDS[1][0] - 10, 0), width=1, color="BLACK")
    window['-GRAPH-'].draw_text(f'{p_data.dates[0]}', (0, -10), color='black', font=None, angle=0)
    window['-GRAPH-'].draw_text(f'{crypto_type}', (-10, 0), color='green', font=32, angle=0,)
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


def draw_settings():
    window = psg.Window('Settings', get_settings_layout())
    is_settings = True
    while is_settings:
        events, values = window.read()
        print(events, values)
        if events in (None, 'Accept'):
            int_combo = window['-INTCOMBO-'].get()
            howlong_combo = window['-HOWLONG-'].get()
            if int_combo == 'day interval':
                SETTINGS['INTCOMBO'] = '1d'
            if int_combo == 'week interval':
                SETTINGS['INTCOMBO'] = '1w'
            if howlong_combo == '7 days':
                SETTINGS['HOWLONG'] = 7
            if howlong_combo == '15 days':
                SETTINGS['HOWLONG'] = 15
            if howlong_combo == '30 days':
                SETTINGS['HOWLONG'] = 30
            if howlong_combo == '90 days':
                SETTINGS['HOWLONG'] = 90
            is_settings = False
    pass


def draw_current_course(p_data: [], window: psg.Window, crypto_type):
    main_text = psg.Text('CURRENT COURSES')
    column = []
    refresh_button = psg.Button('Refresh')
    for coin in p_data:
        column.append([psg.Text(str(coin['symbol'])), psg.Text(str(coin['price']))])
    exit_button = psg.Exit()
    layout = [[main_text], [psg.Column(column)], [refresh_button, exit_button]]
    this_window = psg.Window('Current Courses', layout)
    is_current_course = True
    while is_current_course:
        events, values = this_window.read()
        print(events, values)
        if events in (None, 'Refresh'):
            is_current_course = False
            this_window.close()
            draw_current_course(p_data, window, crypto_type)
        if events in (None, 'Exit'):
            this_window.close()
            is_current_course = False
    return True




def get_settings_layout():
    graph_text = psg.Text('FOR MATH GRAPHS')
    interval_format = psg.Combo(['day interval', 'week interval'], key='-INTCOMBO-')
    interval_format_text = psg.Text('Interval')
    howlong_format = psg.Combo(['7 days', '15 day', '30 days', '90 days'], key='-HOWLONG-')
    howlong_format_text = psg.Text('Area of analysis')
    ok_button = psg.Exit('Accept')
    layout_for_col_graph = [[graph_text],
                            [interval_format, interval_format_text],
                            [howlong_format, howlong_format_text]]
    graph_col = psg.Column(layout_for_col_graph)
    layout = [
             [graph_col],
             [ok_button]
         ]
    return layout


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
    elif event in (None, "Show Current Course"):
        return Returns.SHOW_CRYPTO_COURSE_CURRENT
    elif event in (None, "Settings"):
        return Returns.SHOW_SETTINGS
    elif event in (None, "Bitcoin"):
        main_window['-CRYPTOTYPE-'].update('BTC')
        return Returns.SELECT_BTC
    elif event in (None, "Etherium"):
        main_window['-CRYPTOTYPE-'].update('ETH')
        return Returns.SELECT_ETH
    elif event in (None, "Binance Coin"):
        main_window['-CRYPTOTYPE-'].update('BNB')
        return Returns.SELECT_BNB
    elif event in (None, "Yearn.Finance"):
        main_window['-CRYPTOTYPE-'].update('YFI')
    elif event in (None, "Lightcoin"):
        main_window['-CRYPTOTYPE-'].update('LTC')
        return Returns.SELECT_YFI
    elif event in (None, "PAX Gold"):
        main_window['-CRYPTOTYPE-'].update('PAXG')
        return Returns.SELECT_YFI

    return u_input


def get_crypto_col():
    button_bitcoin = psg.Button("Bitcoin")
    button_etherium = psg.Button("Etherium")
    button_binance_coin = psg.Button("Binance Coin")
    button_waltonchain = psg.Button("Yearn.Finance")
    button_lightcoin = psg.Button("Lightcoin")
    button_paxgold = psg.Button("PAX Gold")
    text_current_type = psg.Text('BTC', key='-CRYPTOTYPE-')

    layout_for_col = [[button_bitcoin, button_etherium, button_binance_coin, button_waltonchain, button_lightcoin, button_paxgold, text_current_type]]

    return psg.Column(layout_for_col, expand_x=True)


def get_options_col():
    button_exit = psg.Exit("Exit")
    button_show_graph = psg.Button("Show Graphic")
    button_show_table = psg.Button("Show Current Course")
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
                                    background_color='white', key="-GRAPH-")

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
