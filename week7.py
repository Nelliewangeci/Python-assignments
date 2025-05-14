
# Iris Dataset Analysis and Visualization

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the dataset
try:
    iris = load_iris(as_frame=True)
    df = iris.frame
    print("Dataset loaded successfully.")
except Exception as e:
    print("Error loading dataset:", e)

# Display the first few rows
print("First few rows of the dataset:")
print(df.head())

# Data types and missing values
print("\nDataset information:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# Cleaning dataset 
df_clean = df.dropna()

# Basic statistics
print("\nBasic statistics:")
print(df_clean.describe())

# Grouping by species (target) and calculating mean
grouped = df_clean.groupby("target").mean()
print("\nMean values grouped by target (species index):")
print(grouped)

# Map target to species names for clarity
df_clean['species'] = df_clean['target'].map(dict(enumerate(iris.target_names)))

# Observations
print("\nInteresting Observations:")
print("Species with the largest average petal length:",
      iris.target_names[grouped['petal length (cm)'].idxmax()])

# Plot 1: Line chart (Sepal length over index)
plt.figure(figsize=(10, 5))
plt.plot(df_clean.index, df_clean["sepal length (cm)"], label="Sepal Length")
plt.title("Sepal Length Over Index")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 2: Bar chart (Average Petal Length per Species)
avg_petal_length = df_clean.groupby("species")["petal length (cm)"].mean()
avg_petal_length.plot(kind='bar', color='skyblue')
plt.title("Average Petal Length per Species")
plt.ylabel("Petal Length (cm)")
plt.xlabel("Species")
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()

# Plot 3: Histogram (Sepal Width distribution)
plt.hist(df_clean["sepal width (cm)"], bins=15, color='salmon', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Plot 4: Scatter Plot (Sepal Length vs. Petal Length)
sns.scatterplot(data=df_clean, x="sepal length (cm)", y="petal length (cm)", hue="species")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.tight_layout()
plt.show()
