import matplotlib.pyplot as plt
import numpy as np

speed = []
rpm = []

with open('../logs/speedlog.txt', 'r') as sl:
    for line in sl:
        speed.append(float(line.split()[0]))

sl.close()

with open('../logs/rpmlog.txt', 'r') as rl:
    for line in rl:
        rpm.append(float(line.split()[0]))

rpm2 = []
with open('../logs/rpmlog3.txt', 'r') as rl2:
    for line in rl2:
        rpm2.append(float(line.split()[0]))


speed2 = []
with open('../logs/speedlog3.txt', 'r') as sl2:
    for line in sl2:
        speed2.append(float(line.split()[0]))

rl.close()

x = []
for i in range(len(speed)):
    x.append(i+1)

x2 = []
for i in range(len(speed2)):
    x2.append(i+1)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex=True)

corr = np.corrcoef(speed, rpm)

color = '#fce5d8'
ax1.set_xlabel('Highway driving - time(s/2) - Rsquared: {0}'.format(corr[0,1]*corr[0,1]))
ax1.set_ylabel('speed', color="#ff392f")
ax1.plot(x, speed, color="#ff392f", linewidth=1.0)
ax1.tick_params(axis='y', labelcolor="#ff392f")
ax1.fill_between(x, 0, speed, color=color)

color = '#b3d2e2'
ax2.set_ylabel('rpm', color="#2873ab")
ax2.plot(x, rpm, color="#2873ab")
ax2.tick_params(axis='y', labelcolor="#2873ab")
ax2.fill_between(x, 0, rpm, color=color)

corr = np.corrcoef(speed2, rpm2)

color = '#fce5d8'
ax3.set_xlabel('City driving - time(s/2) - Rsquared: {0}'.format(corr[0,1]*corr[0,1]))
ax3.set_ylabel('speed', color="#ff392f")
ax3.plot(x2, speed2, color="#ff392f", linewidth=1.0)
ax3.tick_params(axis='y', labelcolor="#ff392f")
ax3.fill_between(x2, 0, speed2, color=color)

color = '#b3d2e2'
ax4.set_ylabel('rpm', color="#2873ab")
ax4.plot(x2, rpm2, color="#2873ab")
ax4.tick_params(axis='y', labelcolor="#2873ab")
ax4.fill_between(x2, 0, rpm2, color=color)




fig.tight_layout()
plt.show()

#plt.plot(x, speed, label='speed')
#plt.plot(x, rpm, label='rpm')
#plt.ylim(0, max(rpm)+5)
#print len(x), x[0]
#plt.xlabel('half seconds')
#plt.legend()
#plt.show()
