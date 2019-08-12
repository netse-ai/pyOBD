from elm327 import ELM327

class OBDI(object):
    def __init__(self):
        self.interface = ELM327(38400, 0.5)

    def connect(self):
        self.interface._connect()

    def cmd(self, cmd):
        return self.interface._command(cmd)

