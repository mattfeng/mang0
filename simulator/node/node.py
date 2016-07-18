from ..generate.generator import *
from abc import ABCMeta, abstractmethod

class Node(object):
    __metaclass__ = ABCMeta

    def __init__(self, name, env, address, profile):
        self.name = name
        self.addr = address
        self.env = env
        self.profile = profile
        self.modulator = None
        self.generator = Generator(env, profile, address)

        self.mk_fps = None      # flows per second

    @abstractmethod
    def run(self, env):
        pass