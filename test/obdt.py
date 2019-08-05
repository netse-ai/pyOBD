import obd

connection = obd.OBD('/dev/rfcomm0')

ports = obd.scan_serial()
print ports

connection = obd.OBD(ports[0], baudrate=38400, check_voltage=False)
