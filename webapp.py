from flask import Flask, render_template
from datetime import datetime
import pandas as pd
import math
import data_processing as dp
import matplotlib as plt

app = Flask(__name__)
df = dp.load_data() #error here


@app.route("/")
def welcome():
  return render_template('welcome.html',
                         message= f"Backend is working, last reload at {datetime.now().time()}"
  )