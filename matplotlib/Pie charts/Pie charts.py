#import sys
#import matplotlib
#from numpy import mat
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()