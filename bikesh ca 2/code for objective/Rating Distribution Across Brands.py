import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Mobile Phone DataSet.csv")

# Plotting
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Rating", y="Brand", hue="Brand", legend=False, palette="coolwarm")
plt.title("Distribution of Mobile Phone Ratings by Brand")
plt.xlabel("Rating")
plt.ylabel("Brand")
plt.tight_layout()
plt.show()
