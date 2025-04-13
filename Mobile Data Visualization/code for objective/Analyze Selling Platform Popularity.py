import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Mobile Phone DataSet.csv")

# Count phones by selling platform
platform_counts = df["Selling Platform"].value_counts()

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(platform_counts.index, platform_counts.values, marker='D', linestyle='-', color='teal', linewidth=2, markersize=10)
plt.title("Number of Phones per Selling Platform (Diamond Line Plot)")
plt.xlabel("Selling Platform")
plt.ylabel("Number of Phones")
plt.grid(True)
plt.tight_layout()
plt.show()
