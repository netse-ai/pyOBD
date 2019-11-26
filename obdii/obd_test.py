import math
import sys
import glob
import pexpect
import bluetooth
from obd import OBDII
from commands import commands


from firebase import firebase
firebase = firebase.FirebaseApplication('https://planit-a12ac.firebaseio.com', None)


#create an OBDI instance
obd = OBDII(baudrate=115200, timeout=0.175)
#connect to elm327
obd.connect()

boost = open('boost_pressure.txt', 'w')

#create a commands object to be passed to obd
cmds = {
    
    commands["INTAKE_PRESSURE"].name: commands["INTAKE_PRESSURE"],
    commands["BAROMETRIC_PRESSURE"].name: commands["BAROMETRIC_PRESSURE"],
}

while True:
    try:
        responses = obd.interface.multi_commands(**cmds)
        intake_pressure = responses['INTAKE_PRESSURE']
        barometric_pressure = responses['BAROMETRIC_PRESSURE']
        boost_pressure = str((intake_pressure - float(barometric_pressure))/6.895)[0:6]
        print "Boost PSI    -------    Boost BARS"
        print boost_pressure + "       -------    " + str(float(boost_pressure) / 14.504)[0:6]
        print >> boost, float(boost_pressure)
        data = '-LudfF76bof48zB80laR'
        snapshot = firebase.put('/obdii/boost', data, {'boost PSI': boost_pressure, 'boost bars' : str(float(boost_pressure) / 14.504)[0:6]}, {'X_FANCY_HEADER': 'VERY FANCY'})
        print snapshot
    except KeyboardInterrupt:
        print "\nFinishing..."
        sys.exit(0)