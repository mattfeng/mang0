import simpy
import numpy as np
from simulator.flow.flow import Flow
from simulator.flow.feature import Feature
from simulator.generate.distribution import *
import random as rnd

fps = {}
fps_variation = []

def read_fps():
    with open('/home/pwn/mang0/profiles/booter1/high/fps/updates.dist') as f:
        f.readline()    # time-series line
        for line in f:
            line = line.strip().split(' ')
            t = int(line[0])
            flows = int(line[1])
            fps[t] = flows

    with open('/home/pwn/mang0/profiles/booter1/high/fps/variation.dist') as f:
        for line in f:
            line = line.strip().split(' ')
            t = int(line[0])
            var = int(line[1])
            fps_variation.append((t, var))

ppf = {}
ppf_variation = []
def read_ppf():
    with open('/home/pwn/mang0/profiles/booter1/high/ppf/updates.dist') as f:
        f.readline()    # time-series line
        for line in f:
            line = line.strip().split(' ')
            t = int(line[0])
            flows = float(line[1])
            ppf[t] = flows

    with open('/home/pwn/mang0/profiles/booter1/high/ppf/variation.dist') as f:
        for line in f:
            line = line.strip().split(' ')
            t = int(line[0])
            var = float(line[1])
            ppf_variation.append((t, var))

ostream = open('udpdnssim.csv', 'w')
ostream.write(Flow.header() + '\n')

def write_flow(flow):
    ostream.write(str(flow) + '\n')

INTERVAL = 1

sips = []
def mk_sips():
    """Makes random source ips"""
    valid = range(0, 256)
    for i in range(0, 340):
        oct1 = rnd.choice(valid)
        oct2 = rnd.choice(valid)
        oct3 = rnd.choice(valid)
        oct4 = rnd.choice(valid)
        sips.append('%s.%s.%s.%s' % (oct1, oct2, oct3, oct4))


def make_flows(env):
    read_fps()
    read_ppf()

    mk_sips()

    flows_var = 0
    ppf_var = 0

    bpp_feature = Feature('bpp', '/home/pwn/mang0/profiles/booter1/high/bpp/',
                          'Bytes Per Packet')

    sipps_feature = Feature('sipps', '/home/pwn/mang0/profiles/booter1/high/sipps/',
                              'Number of Unique Source IPs')

    dur_feature = Feature('dur', '/home/pwn/mang0/profiles/booter1/high/dur/',
                          'Flow Duration')

    feature_set = [bpp_feature,
                   sipps_feature,
                   dur_feature]

    while True:
        for feature in feature_set:
            if len(feature.updates) != 0:
                time_to_update = feature.updates[0][0]
                up_dist_file = feature.updates[0][1]
                if env.now >= time_to_update:
                    feature.generator = mk_generator_from_file(up_dist_file)
                    print '%s updated @ %s' % (feature.name, env.now)
                    feature.updates.pop(0)

        if len(fps_variation) != 0:
            if env.now >= fps_variation[0][0]:
                flows_var = fps_variation[0][1]
                fps_variation.pop(0)

        if len(ppf_variation) != 0:
            if env.now >= ppf_variation[0][0]:
                ppf_var = ppf_variation[0][1]
                ppf_variation.pop(0)

        t = int(env.now)
        nflows = fps[t] + np.random.randint(-flows_var, flows_var + 1)
        pkt_avg = ppf[t] + np.random.uniform(-ppf_var, ppf_var + 1)

        num_uniq_sips = next(sipps_feature.generator)
        sips_to_choose_from = rnd.sample(sips, num_uniq_sips)
        bpp_multiplier = next(bpp_feature.generator)

        for i in range(nflows):
            stime = env.now + np.around(np.random.uniform(0.001, INTERVAL), 3)
            dur = np.around(next(dur_feature.generator), 3)
            proto = 17
            sip = rnd.choice(sips_to_choose_from)
            sp = 53
            dip = '216.9.0.1'
            dp = np.random.randint(0, 2**16)
            iflags = ''
            uflags = ''
            pkt = int(pkt_avg + np.random.uniform(-5, 5))
            # as long as the random is centered around 0, then
            # the extra randomization should be okay
            oct = int(pkt * bpp_multiplier)
            flow = Flow(stime, dur, proto, sip, sp, dip, dp, iflags, uflags, pkt, oct)
            write_flow(flow)

        yield env.timeout(INTERVAL)


env = simpy.Environment()
env.process(make_flows(env))
env.run(until=295)
