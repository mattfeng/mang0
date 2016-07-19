import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import simulator.util.temporal as tmp
from simulator.util.plotter import *
from IPython import embed

sns.set_style('whitegrid')

FILENAME = 'icmp_ping_sim.csv'
dataset(FILENAME)
udp = pd.read_csv(FILENAME, delimiter='|')

TIME_SHIFT = 2208970800.0 - 43200
udp.st = tmp.t2e(udp.stime, TIME_SHIFT)

fps = {}            # GOOD
bpp = {}            # GOOD, COULD BE IMPROVED I THINK
sipps = {}          # GOOD
pps = {}            # GOOD
bps = {}            # GOOD
ppf = {}            # GOOD, COULD BE IMPROVED
dur = udp.dur


features = {'fps'       :fps,
            'bpp'       :bpp,
            'sipps'     :sipps,
            'pps'       :pps,
            'bps'       :bps,
            'ppf'       :ppf,
            }

def f(feature):
    p(features[feature])
    l(feature)
    plt.show()

for i in range(0, 300):
    ST = i
    ET = i + 1
    flows_between = udp[ (udp.st >= ST) & (udp.st < ET) ]

    fps[i] = len(flows_between)
    bpp[i] = (flows_between.oct / flows_between.pkt).mean()
    sipps[i] = len(set(flows_between.sip))
    pps[i] = sum(flows_between.pkt)
    bps[i] = sum(flows_between.oct)
    ppf[i] = flows_between.pkt.mean()

embed()
