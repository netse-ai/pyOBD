class OBDCommand(object):
    def __init__(self,
                 name,
                 description,
                 cmd,
                 byte_length,
                 decoder=None,
                 fast):
        self.name = name
        self.cmd = cmd
        self.description = description
        self.byte_length = byte_length
        self.decoder
        self.fast = fast

    def print_decoder(self):
        print self.decoder
