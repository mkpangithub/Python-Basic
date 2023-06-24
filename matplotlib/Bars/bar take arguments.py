#import sys
#import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

x = ["APPLES", "BANANAS"]
y = [400, 300]

plt.bar(x, y)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()