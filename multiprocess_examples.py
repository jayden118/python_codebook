from multiprocessing import Process, Value, Array, Lock, Pool
from multiprocessing import Queue
import os
import time

def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1


def add_100s(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            for j in range(len(numbers)):
                numbers[j] += 1


def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)


def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)


def cube(number):
    return number * number * number


if __name__ == '__main__':

    lock = Lock()
    shared_number = Value('i', 0) # i -> integer
    shared_array = Array('d', [0.0, 100.0, 200.0]) # d -> double
    print("Number at the beginning is ", shared_number.value)
    print("Array at the beginning is ", shared_array[:])

    p1 = Process(target=add_100, args=(shared_number, lock))
    p2 = Process(target=add_100, args=(shared_number, lock))
    p3 = Process(target=add_100s, args=(shared_array, lock))
    p4 = Process(target=add_100s, args=(shared_array, lock))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("Number at the end is ", shared_number.value)
    print("Array at the end is ", shared_array[:])

    numbers = range(1, 6)

    q = Queue()
    p5 = Process(target=square, args=(numbers, q))
    p6 = Process(target=make_negative, args=(numbers, q))

    p5.start()
    p6.start()

    p5.join()
    p6.join()

    while not q.empty():
        print(q.get())

    numbers = range(10)
    pool = Pool()

    # map, apply, join, close,
    result = pool.map(cube, numbers)
    # pool.apply(cube, numbers[0])

    pool.close()
    pool.join()

    print(result)
