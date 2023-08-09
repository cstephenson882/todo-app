import zipFuntions
import PySimpleGUI as sg
from pathlib import Path

# Create a PySimpleGUI window layout for zip file selection
layout = [
    [sg.Text('Select a zip file to extract:')],
    [sg.InputText(key='zip_file_path'), sg.FileBrowse(file_types=(("Zip Files", "*.zip"),))],
    [sg.Text('Select destination folder for extraction:')],
    [sg.InputText(key='destination_folder'), sg.FolderBrowse()],
    [sg.Button('Extract Zip Archive'), sg.Button('Exit')],
]

# Create the window
window = sg.Window('Extract Zip Archive', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Extract Zip Archive':
        zip_file_path = values['zip_file_path']
        destination_folder = values['destination_folder']

        zipFuntions.unzip_files(zip_file_path,destination_folder)
        sg.popup(f'Zip file contents extracted to "{destination_folder}"')

window.close()
