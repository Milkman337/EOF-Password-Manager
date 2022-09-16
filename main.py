import PySimpleGUI as sg

layout = [
    [sg.Text("Master Password")],
    [sg.Input()],
    [sg.Button("Login")]
]

window = sg.Window("EOF Password Manager", layout)

run = True
while run:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Quit":
        run = False

window.close()