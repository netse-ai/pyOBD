from obd import OBDI
from commands import commands
obd = OBDI()
obd.connect()

with open('speed_log.txt', 'w') as sl:
    pass

while True:
    try:
        print "----------------"
        print obd.cmd(commands["SPEED"]), obd.cmd(commands["RPM"]), obd.cmd(commands["ENGINE_LOAD"]), obd.cmd(commands["COOLANT_TEMP"])
    except KeyboardInterrupt:
        print sl >> str(obd.cmd(commands["SPEED"]))
        raise

# while True:
#     print obd.cmd(commands["SPEED"]), obd.cmd(commands["RPM"])
    # cmds = {
    #     commands["SPEED"].name: commands["SPEED"],
    #     commands["RPM"].name: commands["RPM"]
    # }
    # obd.interface._multiple_commands(**cmds)
