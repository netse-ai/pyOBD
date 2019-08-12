class OBDCommand(object):
    def __init__(self,
                 name,
                 description,
                 cmd,
                 _bytes,
                 fast):
        self.name = name
        self.cmd = cmd
        self.description = description
        self._byes = _bytes
        self.fast = fast
