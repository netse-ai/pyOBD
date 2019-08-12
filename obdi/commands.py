from obdcommand import OBDCommand
   
cmds = [

    OBDCommand("PIDS_A", "Supported PIDS[01-20]", "0100", 6, fast=True),
    OBDCommand("STATUS", "Status since DTCs cleared", "0101", 6, fast=True),
    OBDCommand("SPEED", "Vehicle speed", "010D", 4, fast=True),
    OBDCommand("RPM", "Enginer RPM", "010C", 4, fast=True)
]

class Commands():
    def __init__(self):
        for cmd in cmds:
            if cmd is not None:
                self.__dict__[cmd.name] = cmd

    def __getitem__(self, key):
        if isinstance(key, basestring):
            return self.__dict__[key]
        else:
            print ("Command Error")


commands = Commands()
