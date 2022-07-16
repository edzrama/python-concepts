from threading import Thread


def square_numbers():
    for i in range(1000):
        result = i * i


if __name__ == "__main__":
    threads = []
    num_threads = 10

    # create threads and assign a function for each thread
    for _ in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    # start all threads
    for thread in threads:
        print(f'process {thread.name} starting')
        thread.start()

    # wait for all threads to finish
    # block the main thread until these threads are finished
    for thread in threads:
        print(f'process {thread.name} joining')
        thread.join()
    print("End threads")