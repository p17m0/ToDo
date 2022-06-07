import PySimpleGUI as sg
import pandas as pd

# Add some color to the window
sg.theme('DarkTeal9')
#  Read excel file
EXCEL_FILE = 'stuffs.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout = [
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('Date', size=(15, 1)), sg.InputText(key='Date')],
    [sg.Text('Time', size=(15, 1)), sg.InputText(key='Time')],
    [sg.InputCombo(('LOW', 'NORMAL', 'HIGH'), 'IMPORTANCE', size=(20, 1)),],
    [sg.Text('StuFF', size=(15, 1)), sg.InputText(key='Stuff')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('Simple data entry form', layout)


def clear_input():
    for key in values:
        window[key]('')
    return None


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        new_record = pd.DataFrame(values, index=[0])
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data saved!')
        clear_input()
window.close()
