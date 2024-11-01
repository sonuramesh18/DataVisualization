import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creating a sample dataset with consistent lengths for demonstration
np.random.seed(0)
data = pd.DataFrame({
'Category': ['A', 'B', 'C', 'D', 'E'],
'Values': np.random.randint(10, 100, 5),
'Random_Scatter_X': np.random.randn(5),
'Random_Scatter_Y': np.random.randn(5) * 10 + 20,
'Pie_Values': [15, 25, 35, 10, 15] 
})

# 1. Line Plot
def line_plot():
  plt.figure(figsize=(8, 5))
  plt.plot(data['Category'], data['Values'], marker='D',
color='orange', linewidth=2) # marker to diamond and color to orange
  plt.title("Line Plot")
  plt.xlabel("Category")
  plt.ylabel("Values")
  plt.grid(True)
  plt.savefig("line_plot.png")
  plt.show()

# 2. Bar Plot
def bar_plot():
  plt.figure(figsize=(8, 5))
  plt.bar(data['Category'], data['Values'], color='coral',
edgecolor='black') 
  plt.title("Bar Plot")
  plt.xlabel("Category")
  plt.ylabel("Values")
  plt.savefig("bar_plot.png")
  plt.show()

# 3. Histogram (using generated random data for histogram separately)
def histogram():
  random_hist = np.random.normal(loc=50, scale=10, size=100) #Separate array for histogram
  plt.figure(figsize=(8, 5))
  plt.hist(random_hist, bins=10, color='teal',
edgecolor='black') 
  plt.title("Histogram")
  plt.xlabel("Random Values")
  plt.ylabel("Frequency")
  plt.savefig("histogram.png")
  plt.show()

# 4. Scatter Plot
def scatter_plot():
  plt.figure(figsize=(8, 5))
  plt.scatter(data['Random_Scatter_X'],
data['Random_Scatter_Y'], color='magenta', alpha=0.7,
marker='x')
  plt.title("Scatter Plot")
  plt.xlabel("X Random")
  plt.ylabel("Y Random")
  plt.grid(True)
  plt.savefig("scatter_plot.png")
  plt.show()

# 5. Box Plot
def box_plot():
  plt.figure(figsize=(8, 5))
  plt.boxplot(data['Values'], labels=['Category Values'],
patch_artist=True, boxprops=dict(facecolor='lightgreen')) 
  plt.title("Box Plot")
  plt.ylabel("Values")
  plt.savefig("box_plot.png")
  plt.show()

# 6. Pie Chart
def pie_chart():
  plt.figure(figsize=(6, 6))
  plt.pie(data['Pie_Values'], labels=data['Category'],
  autopct='%1.1f%%', startangle=140,
colors=plt.cm.Accent.colors) 
  plt.title("Pie Chart")
  plt.savefig("pie_chart.png")
  plt.show()
  
# Running each plot function to display and save
line_plot()
bar_plot()
histogram()
scatter_plot()
box_plot()
pie_chart()