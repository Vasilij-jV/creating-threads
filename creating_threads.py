# -*- config: utf8 -*-
from time import sleep
from threading import Thread


def get_numbers():
    for number in range(1, 11):
        sleep(1)
        print(number, flush=True)


def get_letter():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for number_letter in range(10):
        sleep(1)
        print(letters[number_letter], flush=True)


thread = Thread(target=get_numbers)
thread.start()

for i in range(1000000):
    count = i * 3

get_letter()

thread.join()
