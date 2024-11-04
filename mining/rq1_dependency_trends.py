import pandas as pd
import matplotlib.pyplot as plt

# You can download dependency_data.csv here https://mega.nz/file/dIJADCzT#VOdYTl3_RDrQ9XgW-u4A8RAaPUsd6yCbx9uJKbi7idU
data = pd.read_csv("dependency_data.csv")

data['Release_Date'] = pd.to_datetime(data['Release_Date'], unit='ms')

# Extract the year from the release date
data['Year'] = data['Release_Date'].dt.year

# Calculate the average dependency count per year
yearly_avg_dependency = data.groupby('Year')['Dependency_Count'].mean()

plt.figure(figsize=(10, 6))
plt.plot(yearly_avg_dependency.index, yearly_avg_dependency.values, marker='o', linestyle='-')
plt.xlabel("Year")
plt.ylabel("Average Dependency Count")
plt.title("Average Number of Dependencies per Library Release Over Time")
plt.grid()
plt.show()

# Compare averages in the first and last five years
# early_period_avg = yearly_avg_dependency.head(5).mean()
# recent_period_avg = yearly_avg_dependency.tail(5).mean()
# print(f"Average dependencies in early period: {early_period_avg}")
# print(f"Average dependencies in recent period: {recent_period_avg}")
