from obdi import OBDI
import os
import stat

try:
    stat.S_ISBLK(os.stat("/dev/rfcomm0").st_mode)
except:
    os.system("sudo rfcomm bind rfcomm0 00:1D:A5:02:86:67")

ob = OBDI()

ob.run()
