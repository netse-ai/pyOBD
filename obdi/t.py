from obd import OBDI
from commands import commands
obd = OBDI()
obd.connect()

sl = open('speed_log.txt', 'w')

while True:
    try:
        print "----------------"
        print obd.cmd(commands["SPEED"]), obd.cmd(commands["RPM"]), obd.cmd(commands["ENGINE_LOAD"]), obd.cmd(commands["COOLANT_TEMP"])
        print >> sl, obd.cmd(commands["SPEED"])
    except KeyboardInterrupt:
        raise

# while True:
#     print obd.cmd(commands["SPEED"]), obd.cmd(commands["RPM"])
    # cmds = {
    #     commands["SPEED"].name: commands["SPEED"],
    #     commands["RPM"].name: commands["RPM"]
    # }
    # obd.interface._multiple_commands(**cmds)
