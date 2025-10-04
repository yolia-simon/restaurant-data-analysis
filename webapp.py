from flask import Flask, render_template
from datetime import datetime
import pandas as pd
import math

app = Flask(__name__)

data = pd.read_csv("data/adams_restaurant_data.csv")

column_names = ','.join(data.columns) # extracts column headings
print(column_names)


@app.route("/")
def welcome():
  return render_template('welcome.html',
                         message= f"Backend is working, last reload at {datetime.now().time()}"
  )


# def time():
#   return f"Backend is working, last reload at {datetime.now().time()}"














# dates = data['date'].unique().tolist() # extracts all dates, avoiding repeats
# weeks = data['week'].unique().tolist()
# years = data['year'].unique().tolist()
# days = data['day'].unique().tolist()
# categories = data['category'].unique().tolist()
# food_items = data['food_item'].unique().tolist()
# delivery_companies = data['delivery_company'].unique().tolist()
# orders = data['orders'].unique().tolist()
# staff_required = data['staff_required'].unique().tolist()

#print(days[:10]) #first ten