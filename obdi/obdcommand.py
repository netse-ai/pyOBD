class OBDCommand(object):
    def __init__(self,
                 name,
                 description,
                 cmd,
                 byte_length,
                 fast):
        self.name = name
        self.cmd = cmd
        self.description = description
        self.byte_length = byte_length
        self.fast = fast
