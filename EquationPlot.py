from matplotlib import pyplot as plt
import numpy as np

# Storing each function in a different variable
r17 = 2000000000/(pow(x,2.7745))
s17 = 19400000000/(pow(x,3.06))
r18 = 300000000/(pow(x,2.41))
s18 = 351000000/(pow(x,2.41))
r19 = 71731/(pow(x,1.347))
s19 = 116013/(pow(x,1.41))

# Adding each function to the plot with a label
plt.plot(x, r17, label='R2017')
plt.plot(x, s17, label=' S2017')
plt.plot(x, r18, label='R2018')
plt.plot(x, s18, label='S2018')
plt.plot(x, r19, label='R2019')
plt.plot(x, s19, label='S2019')

# Adding titles, legend, gridlines
plt.title('Band 12/SOC Regression Functions')
plt.xlabel('Band 12 Value')
plt.ylabel('SOC Percent')
plt.legend()
#plt.ylim([0, 6])
#plt.xlim([1200, 2500])
plt.grid(alpha=.4,linestyle='--')

# Showing final plot
plt.show()
