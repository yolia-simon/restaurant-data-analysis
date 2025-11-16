import pandas as pd
import matplotlib.pyplot as plt
import math


data = pd.read_csv("data/adams_restaurant_data_updated.csv")

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

#finished creating graph for weekly food consumption here

grouping_2 = data.groupby(['day', 'year', 'category'], as_index=False).size()
grouping_2.rename(columns={'size': 'order_no'}, inplace=True)
year1 = grouping_2[grouping_2['year'] == 2022] #sorting by year
year2 = grouping_2[grouping_2['year'] == 2023]
year3 = grouping_2[grouping_2['year'] == 2024]

#pivoting data changes the columns to the categories and values to the order number
def create_bar_chart(group, year):
  order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

  x = grouping_2[grouping_2['year'] == year]
  y = x.pivot(index='day', columns='category', values='order_no')
  y = y.reindex(order)
  y.plot(kind='bar')
  plt.title(f'Peak Days for Vegan and Mixed Dishes for {year}')
  plt.xlabel('Day of the week')
  plt.ylabel('Number of orders')
  plt.xticks(rotation=45)
  plt.tight_layout()
  return plt.show()

for year in [2022, 2023, 2024]:
  create_bar_chart(grouping_2, year)

#finished creating graphs for peak days for vegan vs mixed food here

grouping_3 = data.groupby(['year', 'delivery_company'], as_index=False).size()
grouping_3.rename(columns={'size': 'order_no'}, inplace=True)

def create_pie_graph(group, year):
  categories = grouping_3['delivery_company']
  select = grouping_3[grouping_3['year'] == year]
  plt.pie(x = select.order_no, autopct='%1.1f%%', shadow=True)
  plt.legend(labels = select.delivery_company, loc = [0.95,0.35])
  plt.title(f'Demand distribution across delivery companies for {year}')
  return plt.show()

for year in [2022, 2023, 2024]:
  create_pie_graph(grouping_3, year)

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