import pandas as pd


try:
  def load_data():
    try:
      data = pd.read_csv("data/adams_restaurant_data_updated.csv")
      # converts column to store order dates
      data['date'] = pd.to_datetime(data['date'],  errors='raise', dayfirst=True, cache=True)
    except:
      raise FileNotFoundError(
        "The CVS file could not be located. Please ensure the file is in the correct place."
      )

    # year = data['year'].unique()  #just to check years in the database
    # print(year)

    return data

    #weekly food consumption data starts here

  def weekly_food_consumption(data):
      # grouping all rows that share the same week and year, then 'flatten' columns for usability
      grouping = data.groupby(['week', 'year'], as_index=False).size().sort_values(by= ['year', 'week'], ascending=[True, True]).rename(columns={'size': 'order_no'})
      # print(grouping.head())
      return grouping

  # creating new column labels for easier plotting         #move to flask appl.
  # week_label = []
  # for year in [22, 23, 24]:
  #     for week in range(1, 53):
  #         week_label.append(f'{year}-W{str(week).zfill(2)}')
  # grouping['week-labels'] = week_label

  # # Define colors for each year
  # year_colors = {2022: 'blue', 2023: 'green', 2024: 'red'}

  # plt.figure(figsize=(12, 5))

  # # Plot each year separately
  # for year, color in year_colors.items():
  #     year_data = grouping[grouping['year'] == year]
  #     plt.plot(year_data['week-labels'], year_data['order_no'], color=color, label=str(year))

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

  #peak days for vegan vs mixed food data starts here

  def peak_days_by_cat(data, year):
    filtered_years = data[data['year'] == year]
    grouping_2 = filtered_years.groupby(['day', 'category'], as_index=False).size().rename(columns={'size': 'order_no'})
    return grouping_2

  #move to flask appl.

  #pivoting data changes the columns to the categories and values to the order number
  #def create_bar_chart(group, year): order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] x = grouping_2[grouping_2['year'] == year] y = x.pivot(index='day', columns='category', values='order_no') y = y.reindex(order) y.plot(kind='bar') plt.title(f'Peak Days for Vegan and Mixed Dishes for {year}') plt.xlabel('Day of the week') plt.ylabel('Number of orders') plt.xticks(rotation=45) plt.tight_layout() return plt.show() for year in [2022, 2023, 2024]: create_bar_chart(grouping_2, year)


  #distr. across delivery companies data starts here

  def delivery_distr(data, year):
    filtered_years = data[data['year'] == year]
    grouping_3 = filtered_years.groupby(['year', 'delivery_company'], as_index=False).size().rename(columns={'size': 'order_no'})
    return grouping_3


  # def create_pie_graph(group, year):    #move to flask appl.
  #     categories = grouping_3['delivery_company']
  #     select = grouping_3[grouping_3['year'] == year]
  #     plt.pie(x = select.order_no, autopct='%1.1f%%', shadow=True)
  #     plt.legend(labels = select.delivery_company, loc = [0.95,0.35])
  #     plt.title(f'Demand distribution across delivery companies for {year}')
  #     return plt.show()
  # for year in [2022, 2023, 2024]:
  #   create_pie_graph(grouping_3, year)

  #KPI card stats data starts here

  def total_orders_per_year(data, year):
    filtered_years = data[data['year'] == year]
    order_per_year = filtered_years.groupby('year').size()
    return order_per_year

  def total_orders_all_time(data):
    total_orders = data['orders'].size()
    return total_orders

  def total_revenue_per_year(data, year):
    filtered_years = data[data['year'] == year]
    yearly_revenue = filtered_years['price'].sum()
    return round(yearly_revenue, 2)

  def total_revenue_all_time(data):
    total_revenue = data['price'].sum()
    return round(total_revenue, 2)

  def most_ordered_per_year(data, year):
    filtered_years = data[data['year'] == year]
    most_ordered = filtered_years['food_item'].value_counts()
    return most_ordered.idxmax(), most_ordered.max()

  # item, count = most_ordered_per_year(data, 2022)
  # print(f"Most ordered item: {item} ({count} orders)")

  def most_ordered_all_time(data):
    most_ordered = data['food_item'].value_counts()
    return most_ordered.idxmax(), most_ordered.max()

  # item, count = most_ordered_all_time(data)
  # print(f"Most ordered item: {item} ({count} orders)")

finally:
  print('The code has run to the end')