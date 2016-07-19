from exporter import Exporter

class TextExporter(Exporter):

    def __init__(self):
        super(TextExporter, self).__init__('txt')

    def process_flow(self, flow):
        return str(flow) + '\n'

