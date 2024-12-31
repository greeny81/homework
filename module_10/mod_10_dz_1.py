import threading
import time
import datetime


stThr = datetime.datetime.now()
thCnt = 0

def write_words(dic, tr):
    global stThr, thCnt
    if tr == 1:
        stThr = datetime.datetime.now()
    st = datetime.datetime.now()
    for count, file_name in  dic.items():
        #print(f'c:{count} v:{file_name}')
        with open(file_name, 'w', encoding='utf-8') as file:
            for i in range(count):
                file.write('Какое-то слово № ' + str(i+1) + '\n')
                time.sleep(0.1)
            print(f'Завершилась запись в файл {file_name}')

    if not tr:
        print(f'Работа потоков {str(datetime.datetime.now() - st)}')
    else:
        thCnt += 1
    if thCnt == 4:
        print(f'Работа threads {str(datetime.datetime.now() - stThr)}')

words = {10: 'example1.txt',30: 'example2.txt', 200: 'example3.txt', 100: 'example4.txt'}

write_words(words,0)
thread = threading.Thread(target=write_words, args=({10: 'example5.txt'},1,))
thread1 = threading.Thread(target=write_words, args=({30: 'example6.txt'},2,))
thread2 = threading.Thread(target=write_words, args=({200: 'example7.txt'},2,))
thread3 = threading.Thread(target=write_words, args=({100: 'example8.txt'},2,))

thread.start()
thread1.start()
thread2.start()
thread3.start()
