import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the TikTok video performance data
data = pd.read_csv('/content/tiktok_performance.csv')

# Display the first few rows to understand the data structure
print(data.head())

# Basic statistics
followers_mean = np.mean(data['User_Followers'])
likes_median = np.median(data['User_Likes'])
following_mode = data['User_Following'].mode()[0]
length_std_dev = np.std(data['Video_Length'])
print(f"Mean Followers: {followers_mean}")
print(f"Median Likes: {likes_median}")
print(f"Mode of Following: {following_mode}")
print(f"Standard Deviation of Video Length: {length_std_dev}")

# Advanced Operation: Calculate Engagement Rate
# Assuming engagement rate as (User_Likes / User_Followers) * 100
data['engagement_rate'] = (data['User_Likes'] /
data['User_Followers']) * 100
print(data[['User_Followers', 'User_Likes','engagement_rate']].head())

# Correlation Analysis
correlation_matrix = data[['User_Followers', 'User_Likes','User_Following', 'Video_Length', 'engagement_rate']].corr()
print("Correlation matrix:")
print(correlation_matrix)

# Visualize the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='viridis')
plt.title('Correlation Matrix of TikTok Performance Metrics')
plt.show()

# Identify Top Performing Videos Based on Engagement Rate
top_videos = data.sort_values(by='engagement_rate',
ascending=False).head(10)
print("Top 10 performing videos based on engagement rate:")
print(top_videos[['Video_ID', 'User_Followers', 'User_Likes','engagement_rate']])