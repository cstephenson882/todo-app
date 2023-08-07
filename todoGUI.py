import PySimpleGUI as sg

import functions

enter_toDo_label = sg.Text('Type a to-do: ')
enter_toDo_textBox = sg.InputText(tooltip='Enter ToDo', key='todos') #tooltip fir hover mouse
add_toDo_button = sg.Button("Add")
list_box = sg.Listbox(values = functions.readToDO(),key ='todo_table',enable_events=True,size=[45,10])
edit_button = sg.Button("Edit")

layout = [ [enter_toDo_label,enter_toDo_textBox,add_toDo_button],
           [list_box,edit_button]

         ]
print(list_box)

window  = sg.Window('To-Do App', layout)

todos = functions.readToDO()
while True:

    event, value = window.read()
    print(event)
    print(value)

    match event:
        case 'Add':
            todos.append(value['todos'] + '\n')
            functions.writeToDo(todos)
            window['todo_table'].update(values=todos)

        case "Edit":
            try:
                edited_todo = value['todos']
                print(todos)
                index_todo = todos.index(value['todo_table'][0])
                todos[index_todo] = edited_todo + '\n'
                functions.writeToDo(todos)
                window['todo_table'].update(values=todos)

            except IndexError:
                continue

        case 'Complete':
            continue
        case 'todo_table':
            window['todos'].update(value = value['todo_table'][0])
        case sg.WINDOW_CLOSED:
            break
        #case True:

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