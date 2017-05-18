import sys
import threading
import time
import random

try:
    import Queue
except:
    import queue as Queue


class packet(object):
    avg = 0
    action = 'Entering'

    def __init__(self, src):
        self.src = src
        if (srce[self.src] != 1):
            self.size = random.randint(0, 100)
        else:
            self.size = random.randint(0, 50)


def coming_packets(sour, delay):
    global qz
    global q
    global max_thres
    for x in range(1, p + 1):
        pack[x] = packet(sour)
        q.put(pack[x])
        if (srce[pack[x].src] == 1):
            time.sleep(0.4)
            srce[pack[x].src] = 0
        for i in range(1, 3):
            if (i == pack[x].src):
                break
        print "Queue size before action:", qz
        if ((qz + pack[x].size) < 500):
            av = (1 - w) * avg[i] + w * (qz + pack[x].size)
            if (av < min_thres):
                pack[x].action = 'Accepted'
                qz = qz + pack[x].size
                pack[x].avg = av
                avg[i] = av
            elif (av > max_thres):
                pack[x].action = 'Dropped'
                srce[i] = 1
            else:
                prob = (av - min_thres) / (max_thres - min_thres)
                print prob
                if (prob < 0.7):
                    pack[x].action = 'Accepted'
                    qz = qz + pack[x].size
                    pack[x].avg = av
                    avg[i] = av
                else:
                    pack[x].action = 'Marked'
                    qz = qz + pack[x].size
                    pack[x].avg = av
                    avg[i] = av
                    srce[i] = 1
        else:
            pack[x].action = 'Dropped'
            srce[i] = 1
            av1 = (1 - w) * avg[i] + w * (qz + pack[x].size)
            max_thres = av1

        print "packet no:", x
        print (avg)
        print "packet size:", pack[x].size
        print "Source:", pack[x].src
        print "Action:", pack[x].action
        print "Queue size after action:", qz
        print srce
        print"------------------"
    global state
    state = 'true'


def going_packets(delay):
    global q
    global state
    global qz
    while (state == 'false'):
        g = q.get()
        time.sleep(delay)
        if ((qz - g.size) >= 0):
            print g.size
            qz = qz - g.size
            print "Queue Size:", qz
            print"-------------------"


if __name__ == '__main__':
    srce = {}
    q = Queue.Queue(10)
    qz = 0
    prob = 0
    max_qz = 2000
    state = 'false'
    for i in range(1, 3):
        srce[i] = 0
    w = 0.2
    min_thres = 100
    max_thres = 500
    x = 0
    pack = {}
    avg = {}
    for i in range(1, 3):
        avg[i] = 0
    p = input("Enter the number of packets:")
    source1 = threading.Thread(target=coming_packets, args=(1, 0.2,))
    source1.start()
    time.sleep(0.3)
    pt = threading.Thread(target=going_packets, args=(0.1,))
    pt.start()
    time.sleep(0.3)
    source2 = threading.Thread(target=coming_packets, args=(2, 0.2,))
    source2.start()