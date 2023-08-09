import zipfile
import pathlib #we use this module because it creates detinational folder paths unique to OS


def zip_files(selected_files,destination_folder,zip_file_name):
    selected_files = selected_files.split(';')

    # Ensure the zip file name has the ".zip" extension
    if not zip_file_name.endswith('.zip'):
        zip_file_name += '.zip'

    # Create a zip archive
    with zipfile.ZipFile(pathlib.Path(destination_folder,zip_file_name), 'w') as zipf:
        for file_path in selected_files:
            file_path = pathlib.Path(file_path)
            zipf.write(file_path, arcname = file_path.name)

def unzip_files(zip_file_path,destination_folder):
    zip_file_path = pathlib.Path(zip_file_path)
    destination_folder = pathlib.Path(destination_folder)

    # Open the zip file and extract its contents
    with zipfile.ZipFile(zip_file_path, 'r') as zipf:
        zipf.extractall(destination_folder)