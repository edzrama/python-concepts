from multiprocessing import Process
import os
import time


def square_numbers():
    for i in range(1000):
        result = i * i
        time.sleep(0.1)


if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()
    print(f'CPU Count = {num_processes}')

    # create processes and assign a function for each process
    for _ in range(num_processes):
        process = Process(target=square_numbers)
        processes.append(process)

    # start all processes
    for process in processes:
        print(f'process {process.name} starting')
        process.start()

    # wait for all processes to finish
    # block the main thread until these processes are finished
    for process in processes:
        print(f'process {process.name} joining')
        process.join()
    print("End processes")