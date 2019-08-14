import sys
from obd import OBDI
from commands import commands


obd = OBDI()
obd.connect()

# sl = open('speed_log.txt', 'w')
# rl = open('rpm_log.txt', 'w')
# el = open('enginer_load_log.txt', 'w')
# cl = open('enginer_coolant_load_log.txt', 'w')

while True:

    cmds = {
        commands["SPEED"].name: commands["SPEED"],
        commands["RPM"].name: commands["RPM"],
        commands["ENGINE_LOAD"].name: commands["ENGINE_LOAD"],
        commands["COOLANT_TEMP"].name: commands["COOLANT_TEMP"]
    }

    print obd.multi_commands(cmds)

    # try:
    #     print "----------------"
    #     speed = obd.cmd(commands["SPEED"])
    #     rpm = obd.cmd(commands["RPM"])
    #     engine_load = obd.cmd(commands["ENGINE_LOAD"])
    #     coolant_tmp = obd.cmd(commands["COOLANT_TEMP"])
    #     print speed, rpm, engine_load, coolant_tmp
    #     print >> sl, speed
    #     print >> rl, rpm
    #     print >> el, engine_load
    #     print >> cl, coolant_tmp
    # except KeyboardInterrupt:
    #     sl.close()
    #     rl.close()
    #     el.close()
    #     cl.close()
    #     sys.exit(0)

#TODO: threading should make this process fast. Slows by a factor of ELM327.timeout for every command
# while True:
#     print obd.cmd(commands["SPEED"]), obd.cmd(commands["RPM"])
    # cmds = {
    #     commands["SPEED"].name: commands["SPEED"],
    #     commands["RPM"].name: commands["RPM"]
    # }
    # obd.interface._multiple_commands(**cmds)
