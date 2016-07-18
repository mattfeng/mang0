from ..config import config
from abc import ABCMeta, abstractmethod

class Exporter(object):
    __metaclass__ = ABCMeta

    def __init__(self, extension):
        outfile = config.OUTFILE + '.' + extension
        self.ostream = open(outfile, 'w')

    @abstractmethod
    def process_flow(self, flow):
        return ''

    def write_flow(self, flow):
        processed_flow = self.process_flow(flow)
        self.ostream.write(processed_flow)

    def close(self):
        self.ostream.close()
