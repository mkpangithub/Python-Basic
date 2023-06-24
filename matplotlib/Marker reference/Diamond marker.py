#import sys
#import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 14])

plt.plot (ypoints, marker = "D")
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
