import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("data/dependency_data.csv")

# Convert Release_Date to datetime
df['Release_Date'] = pd.to_datetime(df['Release_Date'], unit='ms')

df['Year'] = df['Release_Date'].dt.year

# Calculate the average dependency count per year
yearly_avg_dependency = df.groupby('Year')['Dependency_Count'].mean()

# Plot average dependency count over time
plt.figure(figsize=(10, 6))
plt.plot(yearly_avg_dependency.index, yearly_avg_dependency.values, marker='o', linestyle='-')
plt.xlabel("Year")
plt.ylabel("Average Dependency Count")
plt.title("Average Number of Dependencies per Library Release Over Time")
plt.grid()
plt.show()

# Plot year-over-year percentage change in dependency count
plt.figure(figsize=(10, 6))
yearly_avg_dependency.plot(kind='bar', color='skyblue')
plt.title("Year-over-Year Percentage Change in Dependency Count")
plt.xlabel("Year")
plt.ylabel("Percentage Change (%)")
plt.show()

# Box plot of dependency counts by year
plt.figure(figsize=(12, 8))
sns.boxplot(x="Year", y="Dependency_Count", data=df)
plt.title("Distribution of Dependency Counts by Year")
plt.xticks(rotation=45)
plt.show()


# Compare averages in the first and last five years
# early_period_avg = yearly_avg_dependency.head(5).mean()
# recent_period_avg = yearly_avg_dependency.tail(5).mean()
# print(f"Average dependencies in early period: {early_period_avg}")
# print(f"Average dependencies in recent period: {recent_period_avg}")