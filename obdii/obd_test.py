import math
import sys
import glob
import pexpect
import bluetooth
from obd import OBDII
from commands import commands

#access firebase instance
from firebase import firebase
firebase = firebase.FirebaseApplication('https://planit-a12ac.firebaseio.com', None)
#/obdii/boost child
data = '-LudfF76bof48zB80laR'

#create an OBDI instance
obd = OBDII(baudrate=115200, timeout=0.2)

#connect to elm327
obd.connect()

#create a commands object to be passed to obd
cmds = {
    
    commands["INTAKE_PRESSURE"].name: commands["INTAKE_PRESSURE"],
    commands["BAROMETRIC_PRESSURE"].name: commands["BAROMETRIC_PRESSURE"],
}
max_psi = -100
max_bars = -100
min_psi = 0
min_bars = 0
while True:
    try:
        #get obdii responses
        responses = obd.interface.multi_commands(**cmds)

        #intake pressure and barometric pressure readings
        intake_pressure = responses['INTAKE_PRESSURE']
        barometric_pressure = responses['BAROMETRIC_PRESSURE']

        #caluclate boost pressure
        boost_pressure = str((intake_pressure - float(barometric_pressure))/6.895)[0:6]
        #convert to bars
        boost_bars = str(float(boost_pressure) / 14.504)[0:6]
        print "Boost PSI    -------    Boost BARS"
        print boost_pressure + "       -------    " + boost_bars

        if float(boost_pressure) > max_psi:
            max_psi = float(boost_pressure)

        if float(boost_bars) > max_bars:
            max_bars = float(boost_bars)

        if min_psi > float(boost_pressure):
            min_psi = float(boost_pressure)

        if min_bars > float(boost_bars):
            min_bars = float(boost_bars)

        #write boost readings to firebasse
        write = {
            'boost PSI': boost_pressure,
            'boost bars' : str(float(boost_pressure) / 14.504)[0:6],
            'max PSI': str(max_psi),
            'max bars': str(max_bars),
            'min PSI': str(min_psi),
            'min bars': str(min_bars),
        }
        snapshot = firebase.put('/obdii/boost', data, write, {'X_FANCY_HEADER': 'VERY FANCY'})
    
    except KeyboardInterrupt:
        print "\nFinishing..."
        sys.exit(0)