import zipfile

def unzip(file, target_folder):
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(target_folder)