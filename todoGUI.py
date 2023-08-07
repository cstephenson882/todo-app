import PySimpleGUI as sg

import functions

enter_toDo_label = sg.Text('Type a to-do: ')
enter_toDo_textBox = sg.InputText(tooltip='Enter ToDo', key='to-do') #tooltip fir hover mouse
add_toDo_button = sg.Button("Add")

layout = [ [enter_toDo_label,enter_toDo_textBox,add_toDo_button]

         ]
window  = sg.Window('To-Do App', layout)

while True:
    event, value = window.read()
    match event:
        case 'Add':
            todos = functions.readToDO()
            todos.append(value['to-do'] + '\n')
            functions.writeToDo(todos)
        case sg.WINDOW_CLOSED:
            break
window.close()



"""# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.OK(), sg.Cancel()]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events"
while True:
    event, values = window.Read()
    if event in (None, 'Cancel'):
        break

window.Close()"""