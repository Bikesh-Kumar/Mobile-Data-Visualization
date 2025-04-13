import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Mobile Phone DataSet.csv")

# Group by refresh rate and get average screen size
screen_vs_refresh = df.groupby("Refresh Rate (Hz)")["Screen Size (inches)"].mean().reset_index()

# Sort by refresh rate
screen_vs_refresh = screen_vs_refresh.sort_values(by="Refresh Rate (Hz)")

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(screen_vs_refresh["Refresh Rate (Hz)"], screen_vs_refresh["Screen Size (inches)"], 
         marker='o', linestyle='-', color='purple', linewidth=2, markersize=8)
plt.title("Average Screen Size vs Refresh Rate (Line Plot)")
plt.xlabel("Refresh Rate (Hz)")
plt.ylabel("Average Screen Size (inches)")
plt.grid(True)
plt.tight_layout()
plt.show()
