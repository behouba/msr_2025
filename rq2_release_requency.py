import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/dependency_data.csv")

# Convert Release_Date to datetime format and extract the year
df['Release_Date'] = pd.to_datetime(df['Release_Date'], unit='ms')
df['Year'] = df['Release_Date'].dt.year

# Calculate the number of releases per library per year
releases_per_library_year = df.groupby(['Library', 'Year']).size().reset_index(name='Release_Count')

# Calculate the average release count per year
yearly_avg_releases = releases_per_library_year.groupby('Year')['Release_Count'].mean()

# Calculate the median and 75th percentile of release counts per year
yearly_release_stats = releases_per_library_year.groupby('Year')['Release_Count'].agg(['mean', 'median', lambda x: x.quantile(0.75)])
yearly_release_stats.columns = ['Mean', 'Median', '75th_Percentile']

# Plot average release count over time
# plt.figure(figsize=(10, 6))
# sns.lineplot(data=yearly_avg_releases, marker='o', color="blue")
# plt.title("Average Release Frequency per Library Over Time")
# plt.xlabel("Year")
# plt.ylabel("Average Releases per Library")
# plt.show()

# Box plot of release counts by year
# plt.figure(figsize=(12, 8))
# sns.boxplot(x="Year", y="Release_Count", data=releases_per_library_year)
# plt.title("Distribution of Release Counts per Library by Year")
# plt.xticks(rotation=45)
# plt.show()

# Plot year-over-year percentage change in average release frequency
# yearly_pct_change = yearly_avg_releases.pct_change() * 100
# plt.figure(figsize=(10, 6))
# yearly_pct_change.plot(kind='bar', color='skyblue')
# plt.title("Year-over-Year Percentage Change in Release Frequency")
# plt.xlabel("Year")
# plt.ylabel("Percentage Change (%)")
# plt.show()
