import serial
import time
import threading

class ELM327(object):
    def __init__(self, baudrate, timeout):
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None
        
    def _connect(self):
        if !self.ser:
            self.ser = serial.Serial('dev/rfcomm0', baudrate=self.baudrate, timeout=self.timeout)
            if self.ser.isOpen():
                print "Connection with: {0} established".format(self.ser.name)

                self.ser.write('ATZ\r')
                self.ser.write('astp0\r')
                self.ser.write('atho\r')
                print "Testing Connection: ", self.ser.readline().split(' ')
                time.sleep(1)
                self.ser.flushInput()
                self.ser.flushOutput()
                print "Connection Succesful"

    def _command(self, commandType):
        
