from obd import OBDI

obd = OBDI()
obd.connect()

print obd.interface._test_cmd()
