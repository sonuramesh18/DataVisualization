import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Sample agriculture crop yield dataset
data = pd.DataFrame({
'Year': range(2010, 2021),
'Wheat_Yield': np.random.uniform(2.0, 4.0, 11),
'Rice_Yield': np.random.uniform(3.0, 5.0, 11),
'Maize_Yield': np.random.uniform(1.5, 3.5, 11)
})
print(data)

# Crop Yield Over Years
plt.figure(figsize=(10, 6))
plt.plot(data['Year'], data['Wheat_Yield'], label='Wheat Yield',marker='d', linestyle='-', color='orange') # Diamond marker
plt.plot(data['Year'], data['Rice_Yield'], label='Rice Yield',marker='p', linestyle='--', color='blue') # Pentagon marker
plt.plot(data['Year'], data['Maize_Yield'], label='Maize Yield',marker='*', linestyle='-.', color='green') # Star marker

# Adding title and labels
plt.title('Crop Yield Over Years')
plt.xlabel('Year')
plt.ylabel('Yield (tons/hectare)')

# Display legend
plt.legend()
plt.show()

# Average Crop Yield (2010-2020)
average_yields = data[['Wheat_Yield', 'Rice_Yield','Maize_Yield']].mean()
crops = ['Wheat', 'Rice', 'Maize']
plt.figure(figsize=(8, 5))
plt.bar(crops, average_yields, color=['gold', 'lightblue','limegreen']) 

# Adding title and labels
plt.title('Average Crop Yield (2010-2020)')
plt.xlabel('Crop')
plt.ylabel('Average Yield (tons/hectare)')

# Adding text annotations on bars
for i, yield_val in enumerate(average_yields):
  plt.text(i, yield_val + 0.05, f'{yield_val:.2f}',ha='center', color='black')
plt.show()

# Correlation between Wheat and Rice Yield
plt.figure(figsize=(8, 6))
plt.scatter(data['Wheat_Yield'], data['Rice_Yield'],color='magenta', alpha=0.7, edgecolor='black')

# Adding title and labels
plt.title('Correlation between Wheat and Rice Yield')
plt.xlabel('Wheat Yield (tons/hectare)')
plt.ylabel('Rice Yield (tons/hectare)')

# Adding a grid
plt.grid(True)
plt.show()

# Distribution of Rice Yield
plt.figure(figsize=(8, 5))
plt.hist(data['Rice_Yield'], bins=5, color='cyan',
edgecolor='black', alpha=0.7)

# Adding title and labels
plt.title('Distribution of Rice Yield')
plt.xlabel('Rice Yield (tons/hectare)')
plt.ylabel('Frequency')
plt.show()

# Wheat Yield Over Years with Annotation
plt.figure(figsize=(10, 6))
plt.plot(data['Year'], data['Wheat_Yield'], label='Wheat Yield',marker='v', linestyle='-', color='red') # Triangle 

# Find the year with the highest wheat yield
max_yield = data['Wheat_Yield'].max()
max_year = data['Year'][data['Wheat_Yield'].idxmax()]

# Annotation for maximum yield
plt.annotate(f'Highest Yield\n{max_yield:.2f} tons/ha',xy=(max_year, max_yield), xytext=(max_year-1, max_yield+0.2),arrowprops=dict(facecolor='black', arrowstyle='->'),fontsize=10, color='darkred')

# Adding title, labels, and legend
plt.title('Wheat Yield Over Years')
plt.xlabel('Year')
plt.ylabel('Yield (tons/hectare)')
plt.legend()
plt.show()