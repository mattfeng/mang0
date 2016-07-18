import numpy as np
from simulator.util.postfunctions import *
import os

def _binsearch(key, values):
    """
    Searches the values for key.
    :param key: A random, uniformly generated value in the range 0.0 to 1.0
    :param values: A list of cumulative probabilities in sorted order.
    :return: The index to the left in values that contains 'key'

    key = .3
    values = [0.1, 0.2, 0.4, 0.5, 0.9, 1.0]
    --> 2
    """
    return np.searchsorted(values, key)

def generate_val(cdf):
    """
    Generates a random variable from the CDF.

    :param cdf: The cumulative probabilities of different values
    :return: a value randomly chosen from the CDF
    """
    additional = cdf[2][0] # the additional instruction to run after generating a random value

    keys = cdf[0]
    probs = cdf[1]

    randval = np.random.random()
    item = keys[_binsearch(randval, probs)]

    # if the item chosen is a CDF, then use that to generate a value
    if isinstance(item, list):
        item = generate_val(item)

    expr = additional.replace('X', str(item))
    evaluated = eval(expr)
    return evaluated

def cdf_from_file(filename):
    """
    Generates the cumulative probability function from "filename"
    Used in tandem with generate_val(cdf).

    :param filename: the file to read the CDF from
    :return: a list object that can be read into generate_val to generate values
    """
    parent_dir = os.path.abspath(os.path.join(filename, os.pardir)) + '/'
    probs, keys, infos = [], [], []
    with open(filename) as f:
        info = f.readline().strip()
        for line in f.readlines():
            line = line.strip().split(' ')
            value, prob = line[0], float(line[1])
            if line[0].endswith('.txt'):
                value = cdf_from_file(parent_dir + value)
            keys.append(value)
            probs.append(prob)
            infos.append(info)

    return [keys, probs, infos]

def mk_generator_from_file(filename):
    cdf = cdf_from_file(filename)
    while True:
        yield generate_val(cdf)

def mk_generator_from_cdf(cdf):
    while True:
        yield generate_val(cdf)

if __name__ == '__main__':
    print _binsearch(.95, [0.1, 0.2, 0.3, 0.4, 0.5, 0.9, 1.0])
