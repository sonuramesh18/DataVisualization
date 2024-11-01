import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Creating a sample dataset
np.random.seed(0)
data = pd.DataFrame({
'Category': np.random.choice(['A', 'B', 'C'], size=100),
'Values': np.random.normal(50, 15, 100),
'Subcategory': np.random.choice(['X', 'Y'], size=100)
})

# Set a Seaborn theme for improved aesthetics
sns.set_theme(style="darkgrid", palette="muted", font_scale=1.2)

# Plot 1: Bar plot
plt.figure(figsize=(8, 5))
barplot = sns.barplot(x='Category', y='Values', data=data,
estimator=np.mean, errorbar='sd', color='teal', ci=None)
plt.title("Average Values by Category")
plt.xlabel("Category")
plt.ylabel("Mean Value with Standard Deviation")

# Adding custom markers
for bar in barplot.patches:
  bar.set_edgecolor('black') # edge color for each bar
plt.show()

# Set a different theme for the next plot
sns.set_theme(style="white", palette="pastel", font="serif",
font_scale=1.1)
plt.figure(figsize=(8, 5))

# Plot 2: Boxplot
boxplot = sns.boxplot(x='Category', y='Values',
hue='Subcategory', data=data, palette="Set2")
plt.title("Value Distribution by Category and Subcategory")
plt.xlabel("Category")
plt.ylabel("Values")

# Customizing legend and aesthetics
plt.legend(title='Subcategory', loc='upper right')
plt.show()