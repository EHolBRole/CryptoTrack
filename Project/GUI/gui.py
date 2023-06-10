import PySimpleGUI as psg


def draw_graphic(p_data):
    pass


def gui_processing(to_close=False):
    if to_close:
        window.close()
        return "Exit"
    u_input = None  # should be ENUM
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        return "Exit"
    return u_input


psg.theme('DarkAmber')

b1 = psg.Exit("Exit")

t1 = psg.Text("Bitcoin")
t2 = psg.Text("Lol", expand_y=True)
t3 = psg.Text("yyy", expand_x=True)

b2 = psg.Button("test", size=(3, 2))
b3 = psg.Button()

layout_for_col1 = [[b1],
                   [b2,t3]]
col1 = psg.Column(layout_for_col1,expand_y=True)

graph1 = psg.Graph(canvas_size=(255, 255),
                   graph_top_right=(600, 200),
                   graph_bottom_left=(150, 0),
                   background_color='white')

layout = [
    [graph1, col1],
    [b3, t1]
]

window = psg.Window('CryptoTrack', layout)




