from flask import Flask, render_template, url_for
from datetime import datetime
import pandas as pd
import math
import data_processing as dp

app = Flask(__name__)
df = dp.load_data()

@app.route("/")
def welcome():
  return render_template('base.html',
                         message= f"Backend is working, last reload at {datetime.now().time()}",
                         image_url=url_for("static", filename="logo.png")
  )



if __name__ == '__main__':
  app.run()
