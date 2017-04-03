import threading

import os
import time

filename = 'adresses.csv'
num_lines = sum(1 for line in open(filename))
last = os.stat(filename).st_mtime
print num_lines


def file_monitor():
    threading.Timer(5.0, file_monitor).start()
    global last
    this = os.stat(filename).st_mtime
    print this
    while 1:
        if this > last:
            last = this
            ##place your function here
            print "ok"
            time.sleep(5)


file_monitor()
