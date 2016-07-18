from simulator.config import config
import datetime
import time
import numpy as np

def sim2realtime(simtime):
    realtime = config.__start + datetime.timedelta(seconds=simtime)
    str_realtime = realtime.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    return str_realtime

def time2epoch(t, timeshift):
    t = t.split(' ')[1]
    t, ms = t.split('.')
    t = time.mktime(time.strptime(t, '%H:%M:%S'))
    ms = float('.' + ms)
    return t + ms + timeshift

t2e = np.vectorize(time2epoch)

if __name__ == '__main__':
    print sim2realtime(0)
