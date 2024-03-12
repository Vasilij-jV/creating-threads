# -*- config: utf8 -*-
from time import sleep
from threading import Thread, Lock

mutex = Lock()


# Блокировка и разблокировка с помощью методов объекта Lock
def get_numbers():
    for number in range(1, 11):
        sleep(1)
        mutex.acquire()
        print(number, flush=True)
        mutex.release()


# Блокировка и разблокировка с помощью контекстного менеджера
def get_letter():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for number_letter in range(10):
        sleep(1)
        with mutex:
            print(letters[number_letter], flush=True)


thread = Thread(target=get_numbers)
thread.start()

# for i in range(1000000):
#     count = i * 4

get_letter()

thread.join()
