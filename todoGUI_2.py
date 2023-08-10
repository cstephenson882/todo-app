import PySimpleGUI as sg
import time
import functions
import starter

#starter.add_needed_files()
sg.theme('Black')
clock = sg.Text('', key = 'time')
enter_toDo_label = sg.Text('Type a to-do: ')
enter_toDo_textBox = sg.InputText(tooltip='Enter ToDo', key='todos', size = 36) #tooltip fir hover mouse
add_toDo_button = sg.Button(size = 50,key = "Add",image_source='gui_files/images/add.png',
                            tooltip='Add To-Do', mouseover_colors='LightBlue2')

list_box = sg.Listbox(values = functions.readToDO(),key ='todo_table',enable_events=True,size=[47,10])
edit_button = sg.Button(key = 'Edit', size=2, image_source='gui_files/images/pencil.png', tooltip='Edit To-Do', button_color='LightBlue2')

complete_Button = sg.Button(size=2, key="Complete", image_source='gui_files/images/complete.png', tooltip='Complete To-Do', button_color=('Black', 'LightBlue2'))

exit_botton = sg.Button('Exit')


layout = [ [clock],
           [enter_toDo_label,enter_toDo_textBox,add_toDo_button],
           [list_box,edit_button,complete_Button],
           [exit_botton]

         ]
#print(list_box)

window = sg.Window('To-Do App', layout, font = ('Helvetica',20))

todos = functions.readToDO()
while True:
    event, value = window.read(timeout = 200)
    current_date = time.strftime('%b %d, %Y %H:%M:%S')
    window['time'].update(value=current_date)

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
                sg.popup('Please make a selection',font = ('Helvetica',20))
                continue


        case 'Complete':
            #print('active 1')
            try:
                index = todos.index(value['todo_table'][0])
                todos.pop(index)
                functions.writeToDo(todos)
                window['todo_table'].update(values=todos)
                window['todos'].update(value = "")
            except IndexError:
                sg.popup('Please make a selection',font = ('Helvetica',20))
        case 'Exit':
            break
        case 'todo_table':
            window['todos'].update(value=value['todo_table'][0].strip('\n'))
        case sg.WINDOW_CLOSED:
            break
        #case True:

window.close()
