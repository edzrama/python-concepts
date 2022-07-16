# import Lock
from threading import Thread, Lock
import time

value = 0


def increase(locking):
    global value

    # lock the state
    locking.acquire()

    local_value = value
    local_value += 1
    time.sleep(0.1)
    value = local_value

    # unlock the state
    locking.release()


def increase_2(locking):
    global value

    # lock the state-shorter code using with
    with locking:
        local_value = value
        local_value += 1
        time.sleep(0.1)
        value = local_value


if __name__ == "__main__":
    # create a lock
    lock = Lock()

    print('Start value: ', value)

    # pass the lock to the target function
    t1 = Thread(target=increase, args=(lock,))  # notice the comma after lock since args must be a tuple
    t2 = Thread(target=increase_2, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', value)

    print('end main')
