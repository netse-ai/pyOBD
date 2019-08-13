from obd import OBDI
from commands import commands
obd = OBDI()
obd.connect()
print obd.cmd(commands["SPEED"])
print obd.cmd(commands["RPM"])
print obd.cmd(commands["ENGINE_LOAD"])
print obd.cmd(commands["COOLANT_TEMP"])

# while True:
#     print obd.cmd(commands["SPEED"]), obd.cmd(commands["RPM"])
    # cmds = {
    #     commands["SPEED"].name: commands["SPEED"],
    #     commands["RPM"].name: commands["RPM"]
    # }
    # obd.interface._multiple_commands(**cmds)
