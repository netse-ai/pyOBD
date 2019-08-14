from elm327 import ELM327

class OBDI(object):
    def __init__(self, baudrate, timeout):
        self.interface = ELM327(baudrate, timeout)

    def connect(self):
        self.interface.connect()

    def cmd(self, cmd):
        return self.interface.command(cmd)
