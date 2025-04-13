import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Mobile Phone DataSet.csv")

# Prepare data: average price by RAM
ram_price = df.groupby("RAM (GB)")["Price (USD)"].mean().sort_values(ascending=False)

# Explode the largest slice
explode = [0.1 if i == 0 else 0 for i in range(len(ram_price))]

# Generate a unique color for each slice using 'tab20' palette
colors = plt.cm.tab20.colors[:len(ram_price)]

# Plotting
plt.figure(figsize=(8, 8))
plt.pie(ram_price.values, labels=ram_price.index.astype(str) + " GB", autopct="%1.1f%%",
        startangle=140, explode=explode, shadow=True, colors=colors)
plt.title("Average Price Distribution by RAM Size (Exploded Pie Chart)")
plt.tight_layout()
plt.show()
