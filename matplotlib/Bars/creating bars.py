#import sys
#import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()