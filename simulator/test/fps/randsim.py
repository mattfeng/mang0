import simulator.generate.distribution as db
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

x = np.linspace(22, 98, 98 - 22 + 1)
MEAN = 1700
AMP = 600
nflows = np.abs(np.sin(x / 4) * AMP) + MEAN
print nflows
rnflows = []

for i in nflows:      # introduce randomization
    rnflows.append(i + np.random.randint(-300, 300))

plt.ylim([0, 3000])
plt.plot(x, rnflows, lw=0.5)
plt.show()


# fps_gen = db.mk_generator_from_cdf(db.cdf_from_file('/home/pwn/mang0/profiles/booter1/high/fps/22.dist'))


# nodes = []
# NNODES =340
# for x in range(NNODES):
#     nodes.append(np.array([next(fps_gen) for i in range(100)]))
#
#
# acc = nodes[0].copy()
# for x in range(1, NNODES):
#     acc += nodes[x]
#
# print acc
#
#
# # plt.plot(nodes[0], lw=0.5, color='red')
# # plt.ylim([0, 13])
# plt.plot(acc, lw=0.5, color=(1.0, 0.7, 0.2))
# plt.plot(nodes[0] * 340/3 + nodes[1] * 340/3+ nodes[2] * 340/3, lw=0.5, color=(1.0, 0.4, 0.2))
# plt.ylim([0, 3000])
# plt.show()
