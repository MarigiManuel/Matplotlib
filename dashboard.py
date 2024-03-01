import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Load the tips dataset
tips = sns.load_dataset("tips")

# Display the first few rows of the dataset
print(tips.head())


# Visualization 1: Line plot of total bill amount over time
plt.figure(figsize=(8, 4))
plt.plot(tips['total_bill'], label='Total Bill')
plt.title('Total Bill Amount Over Time')
plt.xlabel('Index')
plt.ylabel('Total Bill Amount')
plt.legend()
plt.show()

# Visualization 2: Scatter plot of total bill amount vs. tip amount
plt.figure(figsize=(8, 4))
plt.scatter(tips['total_bill'], tips['tip'])
plt.title('Relationship Between Total Bill Amount and Tip Amount')
plt.xlabel('Total Bill Amount')
plt.ylabel('Tip Amount')
plt.show()

# Visualization 3: Bar plot of average tip amount by day of the week
plt.figure(figsize=(8, 4))
sns.barplot(x='day', y='tip', data=tips, estimator=np.mean)
plt.title('Average Tip Amount by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Average Tip Amount')
plt.show()


# Create a subplot layout for the dashboard
fig, axs = plt.subplots(3, 1, figsize=(10, 12))

# Visualization 1: Line plot
axs[0].plot(tips['total_bill'], label='Total Bill')
axs[0].set_title('Total Bill Amount Over Time')
axs[0].set_xlabel('Index')
axs[0].set_ylabel('Total Bill Amount')
axs[0].legend()

# Visualization 2: Scatter plot
axs[1].scatter(tips['total_bill'], tips['tip'])
axs[1].set_title('Relationship Between Total Bill Amount and Tip Amount')
axs[1].set_xlabel('Total Bill Amount')
axs[1].set_ylabel('Tip Amount')

# Visualization 3: Bar plot
sns.barplot(x='day', y='tip', data=tips, estimator=np.mean, ax=axs[2])
axs[2].set_title('Average Tip Amount by Day of the Week')
axs[2].set_xlabel('Day of the Week')
axs[2].set_ylabel('Average Tip Amount')

plt.tight_layout()
plt.show()
