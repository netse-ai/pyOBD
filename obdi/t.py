from obd import OBDI
from commands import commands
obd = OBDI()
obd.connect()
while True:
    obd.cmd(commands["SPEED"])
    obd.cmd(commands["RPM"])
