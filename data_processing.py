import pandas as pd
import math


data = pd.read_csv("data/adams_restaurant_data.csv")

no_rows = len(data)
# print(no_rows)
no_columns = data.shape
# print(no_columns)
column_names = ' '.join(data.columns) # extracts column headings
# print(column_names)

# grouping all rows that share the same week and year, then 'flatten' columns for usability
grouping = data.groupby(['week', 'year'], as_index=False).size()
grouping = grouping.sort_values(by= ['year', 'week'], ascending=[True, True])
grouping.rename(columns={'size': 'order_no'}, inplace=True)
# print(grouping.head())

# creating new column labels for easier plotting
week_label = []

for x in [2022, 2023, 2024]:
  for y in range(1,53):
    week_no = str(y).zfill(2)
    label = f'{x}-W{week_no}'
    week_label.append(label)
# print(week_label)

# adding column to dataframe
grouping['week-labels'] = week_label
# display(grouping)




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

def total_revenue_per_year(data, year):
  filtered_years = data[data['year'] == year]
  yearly_revenue = filtered_years['price'].sum()

  # total = total_revenue_per_year(data, 2022)   #test code
  # print(f"Revenue: £ {total:.2f}")

  return yearly_revenue

def total_revenue_all_time(data):
  yearly_revenue = data['price'].sum()
  return

def most_ordered_per_year(data, year):
  filtered_years = data[data['year'] == year]
  most_ordered = filtered_years['food_item'].value_counts()

# item, count = most_ordered_per_year(data, 2022)     # test code
# print(f"Most ordered item: {item} ({count} orders)")

  return most_ordered.idxmax(), most_ordered.max() # returns name of item and how many times it appears in a year

def most_ordered_all_time(data):
  most_ordered = data['food_item'].value_counts()
  return most_ordered.idxmax(), most_ordered.max() # returns name of item and how many times it appears in total

