import sys
import glob
import pexpect
import bluetooth
from obd import OBDI
from commands import commands


obd = OBDI(baudrate=38400, timeout=0.25)
obd.connect()

# while True:
#     obd.interface.write_byte_commands(b'010D')
    

sl = open('speed_log.txt', 'w')
rl = open('rpm_log.txt', 'w')
el = open('engine_load_log.txt', 'w')
cl = open('engine_coolant_load_log.txt', 'w')

cmds = {
    commands["SPEED"].name: commands["SPEED"],
    commands["RPM"].name: commands["RPM"],
    commands["ENGINE_LOAD"].name: commands["ENGINE_LOAD"],
    commands["COOLANT_TEMP"].name: commands["COOLANT_TEMP"]
}

while True:
    try:
        responses = obd.interface.multi_commands(**cmds)
        speed = responses['SPEED']
        rpm = responses['RPM']
        engine_load = responses['ENGINE_LOAD']
        coolant_tmp = responses['COOLANT_TEMP']
        print "SPEED\t RPM\t ENGINE_LOAD\t COOLANT_TEMP\t"
        print speed, "\t", rpm, "\t", engine_load, "\t", coolant_tmp
        print >> sl, speed
        print >> rl, rpm
        print >> el, engine_load
        print >> cl, coolant_tmp
    except KeyboardInterrupt:
        print "\nFinishing..."
        sys.exit(0)

# #TODO: threading should make this process fast. Currently slows by a factor of ELM327.timeout for every command
# # while True:
# #     print obd.cmd(commands["SPEED"]), obd.cmd(commands["RPM"])
#     # cmds = {
#     #     commands["SPEED"].name: commands["SPEED"],
#     #     commands["RPM"].name: commands["RPM"]
#     # }
#     # obd.interface._multiple_commands(**cmds)
