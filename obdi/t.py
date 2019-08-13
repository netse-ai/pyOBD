from obd import OBDI
from commands import commands
obd = OBDI()
obd.connect()

sl = open('speed_log.txt', 'w')
rl = open('rpm_log.txt', 'w')
el = open('enginer_load_log.txt', 'w')
cl = open('enginer_coolant_load_log.txt', 'w')
while True:
    try:
        print "----------------"
        speed = obd.cmd(commands["SPEED"])
        rpm = obd.cmd(commands["RPM"])
        el = obd.cmd(commands["ENGINE_LOAD"])
        cl = obd.cmd(commands["COOLANT_TEMP"])
        print speed, rpm, el, cl
        print >> sl, speed
        print >> rl, rpm
        print >> el, el
        print >> cl, cl
    except KeyboardInterrupt:
        sl.close()
        rl.close()
        el.close()
        cl.close()
        raise Exception('Finished logging...')

# while True:
#     print obd.cmd(commands["SPEED"]), obd.cmd(commands["RPM"])
    # cmds = {
    #     commands["SPEED"].name: commands["SPEED"],
    #     commands["RPM"].name: commands["RPM"]
    # }
    # obd.interface._multiple_commands(**cmds)
