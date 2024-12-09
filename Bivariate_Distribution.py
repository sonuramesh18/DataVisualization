import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the Penguins dataset from a local CSV file
penguins = pd.read_csv("C://Users//cheta//Downloads//penguins_dataset.csv")

# Remove rows with missing values
penguins = penguins.dropna()

# Create a jointplot of flipper length vs. bill length
sns.jointplot(
    data=penguins, 
    x="flipper_length_mm", 
    y="bill_length_mm", 
    hue="species",        # Color points by species (only works with scatter)
    kind="scatter",       # Scatter plot to support hue
    palette="coolwarm",  
    height=8              # Increased plot height for better visibility
)

# Display the plot
plt.show()

# Now, creating a hexbin plot without 'hue'
sns.jointplot(
    data=penguins, 
    x="flipper_length_mm", 
    y="bill_length_mm", 
    kind="hex",           # Hexbin plot for a different look
    palette="coolwarm",   
    height=8              # Increased plot height for better visibility
)

# Display the hexbin plot
plt.show()
