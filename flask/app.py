from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
from lets_plot import *
import sqlite3
import requests

# Initialize Lets-Plot
LetsPlot.setup_html()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


### Data processing






















if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, use_reloader=False)