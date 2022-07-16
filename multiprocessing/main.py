import multiprocessing as mp
import threading
import time
import math

result_01 = []
result_02 = []
result_03 = []

def square_a(numbers):
    for number in numbers:
        result_01.append(math.sqrt(number ** 3))


def square_b(numbers):
    for number in numbers:
        result_02.append(math.sqrt(number ** 4))


def square_c(numbers):
    for number in numbers:
        result_03.append(math.sqrt(number ** 5))


if __name__ == '__main__':
    number_list = list(range(1000000))

    start = time.time()
    result_01.append(square_c(number_list))
    result_02.append(square_b(number_list))
    result_03.append(square_c(number_list))
    end = time.time()
    print(f'Duration : {end - start}')

    t1 = mp.Process(target=square_a, args=(number_list,))
    t2 = mp.Process(target=square_b, args=(number_list,))
    t3 = mp.Process(target=square_c, args=(number_list,))
    start = time.time()
    t1.start()
    t2.start()
    t3.start()
    end = time.time()
    print(f'Multiprocessing Duration : {end - start}')
