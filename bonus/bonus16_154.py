import PySimpleGUI as sg
import zipFuntions



layout = [
    [sg.Text('Select files to include in the zip archive:')],
    [sg.InputText(key='selected_files'), sg.FilesBrowse()],
    [sg.Text('Select destination folder for the zip archive:')],
    [sg.InputText(key='destination_folder'), sg.FolderBrowse()],
    [sg.Text('Enter the name of the zip file:')],
    [sg.InputText(key='zip_file_name')],
    [sg.Button('Create Zip Archive'), sg.Button('Exit')],
]

# Create the window
window = sg.Window('Create Zip Archive', layout)


while True:
    event, values = window.read()
    match event:
        case sg.WINDOW_CLOSED:
            break
        case 'Exit':
            break
        case 'Create Zip Archive':
            selected_files = values['selected_files']
            destination_folder = values['destination_folder']
            zip_file_name = values['zip_file_name']

            zipFuntions.zip_files(selected_files, destination_folder, zip_file_name)

            sg.popup(f'Zip archive "{zip_file_name}" created in "{destination_folder}"')

window.close()


