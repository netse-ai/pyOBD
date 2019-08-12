import serial
import time
import threading
import os
import stat
from commands import commands
from serial import SerialException

class ELM327(object):
    def __init__(self, baudrate, timeout):
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None

    def _connect(self):
        print "Attempting to Connect"
        try:
                stat.S_ISBLK(os.stat("/dev/rfcomm0").st_mode)
        except:
            os.system("sudo rfcomm bind rfcomm0 00:1D:A5:02:86:67")
        try:
            self.ser = serial.Serial('/dev/rfcomm0', baudrate=self.baudrate, timeout=self.timeout)
            if self.ser.isOpen():
                print "Connection with: {0} established".format(self.ser.name)

                self.ser.flushInput()
                self.ser.write('ATZ\r')
                self.ser.flushOutput()
                self.ser.flushInput()
                self.ser.write('astp0\r')
                self.ser.flushOutput()
                self.ser.flushInput()
                self.ser.write('ath0\r')
                print "Testing Connection: ", self._read().split(' ')
                time.sleep(1)
                self.ser.flushInput()
                self.ser.flushOutput()
                print "Connection Succesful"
            else:
                print "Connection Error"

        except SerialException:
            print "Serial Exception Error"

    def _command(self, cmd):
        if self.ser.isOpen():
            cmd = cmd.cmd
            cmd += "\r"
            print cmd
            #self.ser.flushInput()
            self.ser.write(cmd)
            print self._read()
            #self.ser.flush()

    def _read(self):
        if self.ser.isOpen():
            data = self.ser.readline().split(' ')
            return data

    def _test_cmd(self):
        if self.ser.isOpen():
            self.ser.write("ATZ\r")
            self.ser.flushInput()
            self.ser.flushOutput()
            if self.ser.readline() != '':
                return self.ser.readline().split(' ')
