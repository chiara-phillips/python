#Import modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import CSV
df = pd.read_csv('/Users/Chiara/Desktop/seqana_challenge/output2.csv')

# Find values for correlation and covariance
corr = df.corr()
#print(corr)
cov = df.cov()
#print(cov)

# Save Correlation and Covariance as CSVs
#corr.to_csv('/Users/Chiara/Desktop/seqana_challenge/corr.csv')
#cov.to_csv('/Users/Chiara/Desktop/seqana_challenge/cov.csv')


# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(14, 14))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(10, 220, as_cmap=True)

# Draw the heatmap
sns.heatmap(corr, 
            cmap=cmap, #palette
            mask=mask, #mask triangle
            vmin= -1, #minimum value
            vmax=1, #max value
            center=0,
            square=True, 
            annot = True, #numbers on squares
            linewidths=.5, 
            cbar_kws={"shrink": .5})

#Add column names to the x axis
ax.set_xticklabels(corr.columns)
#Add column names to the y axis
ax.set_yticklabels(corr.columns)

# Title
title = "SOC Stock and Covariate Correlation"
plt.title(title,fontsize=18)
ttl = ax.title


# fix for mpl bug that cuts off top/bottom of seaborn viz
b, t = plt.ylim() # discover the values for bottom and top
b += 0.5 # Add 0.5 to the bottom
t -= 0.5 # Subtract 0.5 from the top
plt.ylim(b, t) # update the ylim(bottom, top) values

# Saving & visualizing the Seaborn Figure:
plt.savefig('/Users/Chiara/Desktop/seqana_challenge/covariate_plot.png')
plt.show()
