import simpy
import numpy as np
from simulator.generate.distribution import *
import datetime as dt

ostream = open('nodes_340_test2.txt', 'w')

def make_flow(env, ttd, tout):
    FPS_COOLDOWN = 3.0
    fps_last_update = -100

    time_updates = []
    gen0 = mk_generator_from_cdf(cdf_from_file('/home/pwn/mang0/profiles/booter1/high/fps/0.dist'))
    gen22 = mk_generator_from_cdf(cdf_from_file('/home/pwn/mang0/profiles/booter1/high/fps/22.dist'))
    gen98 = mk_generator_from_cdf(cdf_from_file('/home/pwn/mang0/profiles/booter1/high/fps/98.dist'))
    time_updates.append((0, gen0))
    time_updates.append((22, gen22))
    time_updates.append((98, gen98))

    fps_generator = None
    yield env.timeout(tout)

    while env.now < ttd:
        # update distributions
        if len(time_updates) != 0:
            t_update = time_updates[0][0]
            generator = time_updates[0][1]

            if t_update <= env.now:
                fps_generator = generator
                fps_last_update = env.now
                time_updates.pop(0)

        fps = next(fps_generator)
        for i in range(fps):
            t = env.now + np.random.uniform(0.0, 1.0)
            print t
            print >> ostream, t

        yield env.timeout(1)

env = simpy.Environment()
for i in range(340 - 17):
    env.process(make_flow(env, 300, 0))

for i in range(17):
    env.process(make_flow(env, 100, 0))

env.run(until=300)