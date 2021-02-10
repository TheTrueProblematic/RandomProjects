import random
import multiprocessing
import time
import threading
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


trds = 12
times = 0
arra = [0, 0, 0, 0]
complete = 0


def start():
    global times
    global arra
    tim = int(input("Times:"))
    # global d1
    # global d2
    # global sE
    # global sO
    # global dE
    # global dO
    # d1 = 0
    # d2 = 0
    # sE = 0
    # sO = 0
    # dE = 0
    # dO = 0

    times = 0
    arra = [0, 0, 0, 0]

    return tim
    # sameEven = 0
    # sameOdd = 0
    # diffEven = 0
    # diffOdd = 0
    # arra = {sameEven, sameOdd, diffEven, diffOdd}


class myThread(threading.Thread):
    def __init__(self, iterat, nam):
        threading.Thread.__init__(self)
        self.iterat = iterat
        self.nam = nam

    def run(self):
        func(self.iterat, self.nam)


def func(tim, name):
    global times
    global arra
    global d1
    global d2
    global sE
    global sO
    global dE
    global dO
    global complete

    for i in range(tim):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        # sE = arr[0]
        # sO = arr[1]
        # dE = arr[2]
        # dO = arr[3]
        if (i % 2) == 0:
            if d1 == d2:
                arra[0] += 1
            else:
                arra[2] += 1
        else:
            if d1 == d2:
                arra[1] += 1
            else:
                arra[3] += 1
        # arry = [sE, sO, dE, dO]
        # arra = arry
        # return arry
        if (i % 1000000) == 0 & i > 0:
            print("Thread " + str(name) + " crossed " + str(i))

    complete += 1
    if complete >= trds:
        sameEven = arra[0]
        sameOdd = arra[1]
        diffEven = arra[2]
        diffOdd = arra[3]

        totEven = sameEven + diffEven
        totOdd = sameOdd + diffOdd

        probEven = str(sameEven / totEven)
        probOdd = str(sameOdd / totOdd)
        probbyO = str((sameOdd / totOdd) / ((sameEven / totEven) + (sameOdd / totOdd)))
        clear()
        print("probEven: " + probEven + "   probOdd: " + probOdd + "    Total Probabilty of odd: " + probbyO)


def main2():
    global times
    global arra
    times = start()
    process = []
    for i in range(times):
        p = multiprocessing.Process(target=func, args=(times, arra,))
        process.append(p)
        p.start()
        if (i % 10000000) == 0:
            print(i)

    for proc in process:
        proc.join()

    sameEven = arra[0]
    sameOdd = arra[1]
    diffEven = arra[2]
    diffOdd = arra[3]

    totEven = sameEven + diffEven
    totOdd = sameOdd + diffOdd

    probEven = str(sameEven / totEven)
    probOdd = str(sameOdd / totOdd)

    print("probEven: " + probEven + "   probOdd: " + probOdd)


def main():
    global times
    global arra
    times = start()
    thr = round(times / trds)
    thread0 = myThread(thr, 0)
    thread1 = myThread(thr, 1)
    thread2 = myThread(thr, 2)
    thread3 = myThread(thr, 3)
    thread4 = myThread(thr, 4)
    thread5 = myThread(thr, 5)
    thread6 = myThread(thr, 6)
    thread7 = myThread(thr, 7)
    thread8 = myThread(thr, 8)
    thread9 = myThread(thr, 9)
    thread10 = myThread(thr, 10)
    thread11 = myThread(thr, 11)

    thread0.start()
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()
    thread11.start()


if __name__ == '__main__':
    main()
