import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Mobile Phone DataSet.csv")

# Prepare data for plotting
brand_price = df.groupby("Brand", as_index=False)["Price (USD)"].mean().sort_values(by="Price (USD)", ascending=False)

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(data=brand_price, x="Price (USD)", y="Brand", hue="Brand", legend=False, palette="viridis")
plt.title("Average Price by Brand")
plt.xlabel("Average Price (USD)")
plt.ylabel("Brand")
plt.tight_layout()
plt.show()
