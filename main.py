import zipfile
import os

# file in zip
folder_path = 'D:\\Gen\\lesson\\Programming\\MyProject\\python_project\\zipfile\\folder'
txt_path = folder_path + '\\test.txt'
zip_path = folder_path + '\\test.zip'

my_zip = zipfile.ZipFile(zip_path, 'w')
my_zip.write(txt_path, 'test.txt', compress_type=zipfile.ZIP_DEFLATED)

my_zip.close()

# -----
# folder in zip
folder_path = 'D:\\Gen\\lesson\\Programming\\MyProject\\python_project\\zipfile\\folder'
zip_path = folder_path + '\\folder.zip'
folder_path_test = folder_path + '\\folder'

my_zip = zipfile.ZipFile(zip_path, 'w')

for path, sub_folder, files in os.walk(folder_path_test):
    for file in files:
        if file == 'ignore.txt':
            continue
        folder = os.path.join(path, file)
        my_zip.write(folder,
                     os.path.relpath(folder, folder_path_test),
                     compress_type=zipfile.ZIP_DEFLATED)

my_zip.close()
