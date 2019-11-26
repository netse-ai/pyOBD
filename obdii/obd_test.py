import math
import sys
import glob
import pexpect
import bluetooth
from obd import OBDII
from commands import commands


#create an OBDI instance
obd = OBDII(baudrate=115200, timeout=0.175)
#connect to elm327
obd.connect()

#open files for logging
# sl = open('speed_log.txt', 'w')
# rl = open('rpm_log.txt', 'w')
# el = open('engine_load_log.txt', 'w')
# cl = open('engine_coolant_load_log.txt', 'w')
boost = open('boost_pressure.txt', 'w')

#create a commands object to be passed to obd
cmds = {
    # commands["SPEED"].name: commands["SPEED"],
    # commands["RPM"].name: commands["RPM"],
    # commands["ENGINE_LOAD"].name: commands["ENGINE_LOAD"],
    # commands["COOLANT_TEMP"].name: commands["COOLANT_TEMP"],
    commands["INTAKE_PRESSURE"].name: commands["INTAKE_PRESSURE"],
    commands["BAROMETRIC_PRESSURE"].name: commands["BAROMETRIC_PRESSURE"],
    # commands["ENGINE_PERCENT_TQ"].name: commands["ENGINE_PERCENT_TQ"],
}


from firebase import firebase
firebase = firebase.FirebaseApplication('https://planit-a12ac.firebaseio.com', None)

data = "4324234.32"
result = firebase.put('/obdii/boost/-LudfF76bof48zB80laR', data, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
print result
# while True:
#     try:
#         responses = obd.interface.multi_commands(**cmds)
#         # speed = responses['SPEED']
#         # rpm = responses['RPM']
#         # engine_load = responses['ENGINE_LOAD']
#         # coolant_tmp = responses['COOLANT_TEMP']
#         intake_pressure = responses['INTAKE_PRESSURE']
#         barometric_pressure = responses['BAROMETRIC_PRESSURE']
#         boost_pressure = str((intake_pressure - float(barometric_pressure))/6.895)[0:6]
#         # tq = responses['BAROMETRIC_PRESSURE']
#         # print "SPEED\t RPM\t ENGINE_LOAD\t COOLANT_TEMP\t BOOST\t"
#         # print speed, "\t", rpm, "\t", engine_load, "\t", coolant_tmp, "\t\t", boost_pressure, " **** ", str(float(boost_pressure) / 14.504)[0:6]
#         print "Boost PSI    -------    Boost BARS"
#         print boost_pressure + "       -------    " + str(float(boost_pressure) / 14.504)[0:6]
#         # print >> sl, float(speed)
#         # print >> rl, float(rpm)
#         # print >> el, float(engine_load)
#         # print >> cl, float(coolant_tmp)
#         print >> boost, float(boost_pressure)
        # data = {'boost pressure': str(boost_pressure)}
        # snapshot = firebase.post('/obdii/-LudcNKKVvXuMSAal7Cx', data)

    # except KeyboardInterrupt:
    #     print "\nFinishing..."
        # sys.exit(0)

# #TODO: threading should make this process fast. Currently slows by a factor of ELM327.timeout for every command
# # while True:
# #     print obd.cmd(commands["SPEED"]), obd.cmd(commands["RPM"])
#     # cmds = {
#     #     commands["SPEED"].name: commands["SPEED"],
#     #     commands["RPM"].name: commands["RPM"]
#     # }
#     # obd.interface._multiple_commands(**cmds)
