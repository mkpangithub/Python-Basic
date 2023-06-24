#import sys
#import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 1, 8, 10])

plt.plot(ypoints, marker = "H")
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()