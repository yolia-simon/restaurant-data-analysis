import pandas as pd
import math
import matplotlib.pyplot as plt


data = pd.read_csv("data/adams_restaurant_data.csv")

no_rows = len(data)
# print(no_rows)
no_columns = data.shape
# print(no_columns)
column_names = ' '.join(data.columns) # extracts column headings
# print(column_names)

# data for 2022
for week in range(1,53):
  data_2022 = data.loc[(data['week'] == week) & (data['year'] == 2022)]
#print(data_2022)

# data for 2023
for week in range(1,53):
  data_2023 = data.loc[(data['week'] == week) & (data['year'] == 2023)]
#print(data_2023)

# data for 2024
for week in range(1,53):
  data_2024 = data.loc[(data['week'] == week) & (data['year'] == 2024)]
#print(data_2024)

# converts column to store order dates
data['date'] = pd.to_datetime(data['date'],  errors='raise', dayfirst=True, cache=True)

# grouping all rows that share the same week and year, then 'flatten' columns for usability
grouping = data.groupby(['week', 'year'], as_index=False).size()
grouping = grouping.sort_values(by= ['year', 'week'], ascending=[True, True])
grouping.rename(columns={'size': 'order_no'}, inplace=True)
# print(grouping.head())

week_label = [] # creating new column labels for easier plotting
for year in [22, 23, 24]:
    for week in range(1, 53):
        week_label.append(f'{year}-W{str(week).zfill(2)}')
grouping['week-labels'] = week_label

# Define colors for each year
year_colors = {2022: 'blue', 2023: 'green', 2024: 'red'}

plt.figure(figsize=(12, 5))

# Plot each year separately
for year, color in year_colors.items():
    year_data = grouping[grouping['year'] == year]
    plt.plot(year_data['week-labels'], year_data['order_no'], color=color, label=str(year))

# plt.title('Weekly Food Consumption Patterns')
# plt.xlabel('Time')
# plt.ylabel('Number of orders')

# # Rotate x-axis labels
# plt.xticks(rotation=45)

# # Show only every 4th label to reduce clutter
# plt.gca().set_xticks(grouping['week-labels'][::4])

# # Add a legend for the colors
# plt.legend(title='Year')

# plt.tight_layout()
# plt.show()