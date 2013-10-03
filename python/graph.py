#!/usr/bin/python
import matplotlib.pyplot as plt

month = [4, 5, 6, 7, 8, 9]
expense = [758.19, 942.77, 863.38, 749.51, 674.18, 642.26]
plt.plot(month, expense)
plt.xlabel('month')
plt.ylabel('expense')
plt.show()
