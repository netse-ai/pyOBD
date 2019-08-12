from obd import OBDI
from commands import commands
obd = OBDI()
obd.connect()
obd.cmd(commands["SPEED"])
