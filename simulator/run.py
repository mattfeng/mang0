import simpy

def main():
    env = simpy.Environment()

    env.run(until = 300)

if __name__ == '__main__':
    main()

