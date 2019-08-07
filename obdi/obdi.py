import serial
import time
import threading

class OBDI(object):

    def __init__(self):
        self.cmd = None
        self.ser = serial.Serial('/dev/rfcomm0', baudrate=38400, timeout=0.5)
        if self.ser:
            print self.ser.name
        self.speed = 'No Data'
        self.rpm = 'No Data'
        self.tmp = 'No Data'
        self.tp = 'No Data'
        self.dtc = 'No Data'
        self.speed_log = []
        self.rpm_log = []
        self.tmp_log = []
        self.tp_log = []
        self.thread_list = []
        self.initializeOBD()

    def initializeOBD(self):
        if self.ser.isOpen():
            self.ser.write('ATZ\r')
            self.ser.write('atsp0\r')
            self.ser.write('ath0\r')
            print "Testing: ", self.ser.readline().split(' ')
            time.sleep(1)
            self.ser.flushInput()
            self.ser.flushOutput()
            print "OBDI intialized"

    def get_speed(self):
        if self.ser.isOpen():
            self.ser.write('01 0D\r')
            speed = self.ser.readline().split(' ')
            speed = speed[(len(speed) - 2)]
            self.speed = float(int('0x' + speed, 0)) * .6214
            self.speed_log.append(self.speed)
            return self.speed

    def get_rpm(self):
        if self.ser.isOpen():
            self.ser.write('01 0C\r')
            rpm = self.ser.readline().split(' ')
            self.rpm = rpm
            #print self.rpm
            lower = rpm[len(rpm)-2]
            upper = rpm[len(rpm)-3]
            lower = float(int('0x' + lower, 0))
            upper = float(int('0x' + upper, 0)) * 256
            self.rpm = (lower + upper) / 4
            self.rpm_log.append(self.rpm)
            return self.rpm

    def get_coolant_tmp(self):
        if self.ser.isOpen():
            self.ser.write('01 05\r')
            tmp = self.ser.readline().split(' ')
            tmp = tmp[len(tmp)-2]
            tmp = float(int('0x' + tmp, 0)) - 40
            tmp = (tmp * (9/5)) + 32
            self.tmp = tmp
            return self.tmp

    def get_throttle_position(self):
        if self.ser.isOpen():
            self.ser.write('01 11\r')
            tp = self.ser.readline().split(' ')
            tp = tp[len(tp)-2]
            tp = float(int('0x' + tp, 0))
            tp = (100/255) * tp
            self.tp = tp
            return self.tp

    def get_DTC(self):
        if self.ser.isOpen():
            self.ser.write('03\r')
            dtc = self.ser.readline().split(' ')
            self.dtc = dtc
            return self.dtc

    def write_logs(self):
        with open('speedlog.txt', 'w') as sl:
            for item in self.speed_log:
                print >> sl, item
        
        with open('rpmlog.txt', 'w') as rl:
            for item in self.rpm_log:
                print >> rl, item

        

    def handle_threads(self):
        speed_thread = threading.Thread(target=self.get_speed)
        self.thread_list.append(speed_thread)
        rpm_thread = threading.Thread(target=self.get_rpm)
        self.thread_list.append(rpm_thread)

    def run(self):
        while True:
            try:
                print "----------------"
                print self.get_speed(), self.get_rpm(), self.get_coolant_tmp(),\
                        self.get_throttle_position()
            except KeyboardInterrupt:
                self.write_logs()        
                raise
