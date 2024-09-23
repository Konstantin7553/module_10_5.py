import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
         line = file.readline()
         while line:
             all_data.append(line)
             line = file.readline()


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start_time = time.time()
for name in filenames:
    read_info(name)
end_time = time.time()
print(f"Линейное время: {end_time - start_time}")

if __name__ == '__main__':
    start_time = time.time()
    with Pool() as p:
        p.map(read_info, filenames)
        end_time = time.time()
        print(f"Многопроцессное время: {end_time - start_time}")



