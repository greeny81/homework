import os, time

dir = 'module_7'
if os.path.exists(dir):
    os.chdir(dir)
print('Current dir: ', os.getcwd())
for file in os.listdir():
    if os.path.isfile(file):
        filepath = os.path.join(os.getcwd(), file)
        filetime = os.path.getmtime(file)
        filesize = os.stat(file).st_size
        formatted_time = time.strftime("%d-%m-%Y %H:%M", time.localtime(filetime))
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
              f' Время изменения: {formatted_time} , Родительская директория: {parent_dir}')

