#!/usr/bin/python
import matplotlib.pyplot as plt

month = [4, 5, 6, 7, 8, 9]
expense = [758.19, 942.77, 863.38, 749.51, 674.18, 642.26]
plt.plot(month, expense, 'ro')
for x, y in zip(month, expense):
	plt.annotate(str(y), xy = (x, y), xytext = (-20, 20),
	textcoords = 'offset points', ha = 'right', va = 'bottom',
	bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
	arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))


plt.xlabel('month')
plt.ylabel('expense')
plt.show()
