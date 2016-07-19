import simpy
import numpy as np
from simulator.export import textexporter
from simulator.flow.flow import Flow

RESOLUTION = 1

def make_flows(env):


    while True:
        # TODO: ALL OF THIS
        proto = 1
        stime = env.now + np.random.uniform(0.001, RESOLUTION)
        dur = 0             # TODO
        sip = '0.0.0.0'     # TODO
        dip = '216.9.0.1'
        iflags = ''
        uflags = ''
        dp = 2048
        sp = 0
        pkt = 1             # TODO
        oct = 1             # TODO


        flow = Flow(stime, dur, proto, sip, sp, dip, dp, iflags, uflags, pkt, oct)
        export.write_flow(flow)
        # TODO: GENERATE THE RESPONSE


        yield env.timeout(RESOLUTION)

export = textexporter.TextExporter()

env = simpy.Environment()
env.process(make_flows(env))
env.run(until=295)