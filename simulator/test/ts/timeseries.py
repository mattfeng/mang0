import simpy

RESOLUTION = 1          # represents 1 second

def make_flows(env):
    while True:

        env.timeout(1)

env = simpy.Environment()
env.process(make_flows(env))
env.run(until=295)