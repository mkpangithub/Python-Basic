#import sys
#import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

x = (["A", "B","C","D"])
y = ([3, 8, 1, 10])

plt.bar(x, y, color = "#4CAF50")
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()