#import sys
#import matplotlib
#matplotlib.use('Agg')


import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylables = ["Apples","Bananas", "Cherrys", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels= mylables, colors= mycolors)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()