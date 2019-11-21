import serial
import time
import threading
import os
import stat
import bluetooth
from commands import commands
from serial import SerialException
from elm327_error import ELM327_Error

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
            print "rfcomm0 exists"
        except:
            os.system("sudo rfcomm bind rfcomm0 00:1D:A5:02:86:67")
        try:
            self.ser = serial.Serial('/dev/rfcomm0', baudrate=self.baudrate, timeout=self.timeout)
            if self.ser.isOpen():
                print "Connection with: {0} established".format(self.ser.name)
                self.command("ATSP0")
                self.command("ATZ")
                self.command('ASTP0')
                self.command('ATH0')
                print "Testing Connection Read"
                try:
                    read = self.read()
                    print "Connection Succesful"
                except:
                    raise ELM327_Error("Read error")
                time.sleep(1)
            else:
                print "Connection Error"

        except SerialException:
            print "Serial Exception Error"

    def monitor_all(self):
        if self.ser.isOpen():
            while True:
                print self.command("ATMA")

    def command(self, cmd):
        if self.ser.isOpen():
            if hasattr(cmd, 'cmd'):
                msg = cmd.cmd
                msg += "\r"
                self.write(msg)
                return self.read(cmd.byte_length, cmd.decoder)
            else:
                msg = cmd
                msg += '\r'
                self.write(msg)
                return self.read()

    def read(self, byte_length=None, decoder=None):
        if self.ser.isOpen():
            data = self.ser.readline().split(' ')
            # print data
            if byte_length == 1:
                data = data[-2]
            elif byte_length == 2:
                data = data[-2].join(data[-3])
            if decoder != None:
                try:
                    data = decoder(data)
                    #Issue with returning in a try/except?
                    # return decoder(data)
                except ValueError:
                    #return None
                    data = None
            return data

    def write(self, cmd):
        cmd += "01"
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

    def write_byte_commands(self, byte_command):
        if self.ser.isOpen():
            byte_command += '\r'
            self.ser.write(byte_command)
            #print self.ser.readline()

    def multi_commands(self, **kwargs):
        responses = {}
        if kwargs is not None:
            for k, v in kwargs.iteritems():
                responses[k] = self.command(v)
        return responses