from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
from lets_plot import ggplot, geom_line, aes, LetsPlot, ggsave
# from lets_plot.export import to_html
# import sqlite3

# Initialize Lets-Plot
LetsPlot.setup_html()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


### Data processing ###
@app.route('/get_plot')
def get_plot():
    
    
    csv_path = 'weekly_adjusted_IBM.csv'

    # Load data into dataframe
    df = pd.read_csv(csv_path)

    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Create a plot
    plot = (
        ggplot(df, aes(x='timestamp', y='adjusted_close')) 
        + geom_line()
    )

    plot_file = 'templates/plot.html'
    ggsave(plot, plot_file)

    with open(plot_file) as f:
        plot_html = f.read()


    return plot_html


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, use_reloader=False)