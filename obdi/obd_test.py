import sys
from obd import OBDI
from commands import commands


obd = OBDI(baudrate=38400, timeout=0.25)
obd.connect()

sl = open('speed_log.txt3', 'w')
rl = open('rpm_log.txt3', 'w')
el = open('enginer_load_log.txt3', 'w')
cl = open('enginer_coolant_load_log.txt3', 'w')

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
        print "Finishing..."
        sys.exit(0)

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
