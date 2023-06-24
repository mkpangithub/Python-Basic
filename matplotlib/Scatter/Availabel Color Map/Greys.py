#import sys
#import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, cmap='Greys_r')

plt.colorbar()

plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()