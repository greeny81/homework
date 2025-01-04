import  multiprocessing
import os
import time
import  threading
import datetime
from multiprocessing import  Pool


filenames = [f'./file {number}.txt' for number in range(1, 5)]


def read_info(name):
    all_data = []

    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


if __name__ == "__main__":
    print(f'os.process_cpu_count: {os.process_cpu_count()}')
    pool = Pool()
    start = datetime.datetime.now()
    results = pool.map(read_info, filenames)
    print(f'Multiprocess: {datetime.datetime.now() - start}')

    start = datetime.datetime.now()
    for i in filenames:
        read_info(i)
    print(f'For {datetime.datetime.now() - start}')