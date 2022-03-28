# import all modules
import pandas as pd
import matplotlib.pyplot as plt
  
# Read in the DataFrame. Change line below to direct to new CSV
df = pd.read_csv('/Users/Chiara/Desktop/seqana_challenge/output2.csv')

# plotting histogram
plt.hist(df['soc_stock_'],bins = 10,
         alpha = 1, color = 'navy')
plt.title('Soil Samples Histogram', fontsize=18)
plt.xlabel("SOC Stock")
plt.ylabel("Count")

plt.show()


# block 1 - simple stats
mean = df['soc_stock_'].mean()
median = df['soc_stock_'].median() 
std = df['soc_stock_'].std() 

# print block 1
print ('Mean: ' + str(mean))
print ('Median: ' + str(median))
print ('Std: ' + str(std))
