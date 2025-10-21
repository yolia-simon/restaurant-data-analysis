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
for x in [2022, 2023, 2024]:
  for y in range(1,53):
    week_no = str(y).zfill(2)
    label = f'{x}-W{week_no}'
    week_label.append(label)
# print(week_label)
grouping['week-labels'] = week_label # adding column to dataframe
# display(grouping)

x_axis = grouping['week-labels']
y_axis = grouping['order_no']

# plt.plot(x_axis, y_axis)
# plt.title('Weekly Food Consumption Patterns', loc='center')
# plt.xlabel('Time')
# plt.ylabel('Number of orders')
# plt.grid(axis='x')
# plt.show()

