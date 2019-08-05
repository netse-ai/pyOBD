import matplotlib.pyplot as plt
import numpy as np

speed = []
rpm = []

with open('speedlog3.txt', 'r') as sl:
    for line in sl:
        speed.append(float(line.split()[0]))

sl.close()

with open('rpmlog3.txt', 'r') as rl:
    for line in rl:
        rpm.append(float(line.split()[0]))

rl.close()

print len(speed), len(rpm)

x = []
for i in range(len(speed)):
    x.append(i+1)

fig, ax1 = plt.subplots()

corr = np.corrcoef(speed, rpm)

color = 'tab:red'
ax1.set_xlabel('time(s/2) - {0}'.format(corr[0,1]*corr[0,1]))
ax1.set_ylabel('speed', color=color)
ax1.plot(x, speed, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('rpm', color=color)
ax2.plot(x, rpm, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()

#plt.plot(x, speed, label='speed')
#plt.plot(x, rpm, label='rpm')
#plt.ylim(0, max(rpm)+5)
#print len(x), x[0]
#plt.xlabel('half seconds')
#plt.legend()
#plt.show()
