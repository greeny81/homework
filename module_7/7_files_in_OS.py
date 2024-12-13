import os

print('Current dir: ', os.getcwd())
dir = 'test_os'
if os.path.exists(dir):
    os.chdir(dir)
else:
    os.mkdir(dir)
    os.chdir(dir)
print('Current dir: ', os.getcwd())
#os.makedirs(r'test1\test2')
#print(os.listdir())
# for i in os.walk('.'):
#     print(i)
os.chdir(r'E:\univerPython\pythonProject1\module_7')
print('Current dir: ', os.getcwd())
print(os.listdir())

file = [f for f in os.listdir() if os.path.isfile(f)] #ГЕНЕРАТОР СПИСКОВ
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print('DIRS:',dirs)
print('FILES: ', file)
#os.startfile(file[8])#запускает 'products.txt' в NOTEPAD FILES:  ['7_bytes_codir.py', '7_files_in_OS.py', ,....
print(os.stat(file[0])) # info about file
print(os.stat(file[0]).st_size, ' bytes')
#os.system('pip install random2')#Successfully installed random2-1.0.2

