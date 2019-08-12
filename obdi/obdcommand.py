class OBDCommand(object):
    def __init__(self,
                 name,
                 cmd,
                 description,
                 _bytes,
                 fast):
        self.name = name
        self.description = description
        self._byes = _bytes
        self.fast = fast
