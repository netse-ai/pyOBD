import serial
import time
import threading
import os
import stat
import bluetooth
from commands import commands
from serial import SerialException

class ELM327(object):
    def __init__(self, baudrate, timeout):
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None
        self.threads = []

    def connect(self):

        print "Attempting to Connect"
        #TODO: Finding the address of the device does not seem to work
        # root permissions are required if you try to manually create rfcomm socket using bluetooth
        #
        # try:
        #     stat.S_ISBLK(os.stat("/dev/rfcomm0").st_mode)
        # except:
        #     nearby_devices = bluetooth.discover_devices(lookup_names=True)
        #     print "NEAR BY DEVICES?"
        #     bd_addr = None
        #     for addr, name  in nearby_devices:
        #         print addr, name
        #         if name == "OBDII":
        #             bd_addr = addr
        #     os.system("sudo rfcomm bind rfcomm0 " + bd_addr)
        #     print "sudo rfcomm bind rfcomm0 " + bd_addr == "sudo rfcomm bind rfcomm0 00:1D:A5:02:86:67"
        #
        try:
            stat.S_ISBLK(os.stat("/dev/rfcomm0").st_mode)
        except:
            os.system("sudo rfcomm bind rfcomm0 00:1D:A5:02:86:67")
        try:
            self.ser = serial.Serial('/dev/rfcomm0', baudrate=self.baudrate, timeout=self.timeout)
            if self.ser.isOpen():
                print "Connection with: {0} established".format(self.ser.name)
                self.write("ATZ\r")
                self.write('ASTP0\r')
                # self.write('ATH0\r')
                print "Testing Connection Read"
                try:
                    read = self.read()
                    print read
                    print "Connection Succesful"
                except:
                    print "Read Error"
                time.sleep(1)
            else:
                print "Connection Error"

        except SerialException:
            print "Serial Exception Error"

    def monitor_all(self):
        if self.ser.isOpen():
            while True:
                self.write("ATMA\r")
                print self.read()

    def command(self, cmd):
        if self.ser.isOpen():
            msg = cmd.cmd
            msg += "\r"
            self.write(msg)
            return self.read(cmd.byte_length, cmd.decoder)

    def read(self, byte_length=None, decoder=None):
        if self.ser.isOpen():
            data = self.ser.readline().split(' ')
            print data
            if byte_length == 1:
                data = data[-2]
            elif byte_length == 2:
                data = data[-2].join(data[-3])
            if decoder != None:
                try:
                    return decoder(data)
                except ValueError:
                    #return a number that can never be reached
                    return 1000000001
            return data

    def write(self, cmd):
        if self.ser.isOpen():
            try:
                self.ser.flushInput()
                self.ser.write(cmd)
                self.ser.flush()
            except Exception:
                self.ser.close()
                print "Error: Writing"
        else:
            "Device not connected."

    def multi_commands(self, **kwargs):
        responses = {}
        if kwargs is not None:
            for k, v in kwargs.iteritems():
                responses[k] = self.command(v)
        return responses
