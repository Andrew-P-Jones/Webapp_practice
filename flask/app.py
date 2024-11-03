from flask import Flask, request, jsonify, render_template
import pandas as pd
# import numpy as np
from lets_plot import *
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
        ggplot(df, aes(x='timestamp', y='adjusted close')) 
        + geom_line()
        + ggtitle('IBM stock price', subtitle='Based on weekly adjusted close prices')
        + xlab('Date')
        + ylab('USD')
    )

    # Save the plot to a html file
    plot_file = ggsave(plot, 'plot1.html')
    # read teh html file into a string 
    with open(plot_file) as file:
        plot_html = file.read()

    # return the html string to the javascript loadplot function
    return plot_html

@app.route('/get_table_data')
def get_table_data():
    csv_path = 'weekly_adjusted_IBM.csv'
    
    # Load data into DataFrame
    df = pd.read_csv(csv_path)
    
    # Filter the columns to display and make an explicit copy
    df_filter = df[['timestamp', 'high', 'low', 'adjusted close']].copy()

    # Calculate the high-low difference and add it as a new column
    df_filter['high_low_diff'] = df_filter['high'] - df_filter['low']               ### Aggregate

    # Round each numeric column to 2 decimal places
    numeric_columns = ['high', 'low', 'high_low_diff', 'adjusted close']
    df_filter[numeric_columns] = df_filter[numeric_columns].round(2)

    # Filter rows where high_low_diff is greater than 20
    df_filter = df_filter[df_filter['high_low_diff'] > 20]                          ### Filter

    # Sort by high_low_diff in descending order
    df_filter = df_filter.sort_values(by='high_low_diff', ascending=False)          ### Sort

    # Convert DataFrame to JSON and return it
    data = df_filter.to_dict(orient='records')
    return jsonify(data)


### Some questions to answer ###
# 1. What is the average adjusted close price for IBM stock per month?
# 2. What is the average high-low difference for IBM stock per year?
# 3. Which year had the greatest change in adjusted close price? (show both the largest gain and loss)


# Question 1
@app.route('/get_monthly_avg')
def get_monthly_avg():
    # read the csv and convert the timestamp to datetime
    csv_path = 'weekly_adjusted_IBM.csv'
    df = pd.read_csv(csv_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # extract the month from the timestamp
    df['month'] = df['timestamp'].dt.month
    df_grouped = df.groupby('month').agg({'adjusted close': 'mean'}).reset_index()
    plot = (
        ggplot(df_grouped, aes(x='month', y='adjusted close')) 
        + geom_line()
        + ggtitle('IBM monthly average stock price', subtitle='Averaged from 1999-2024')
        + xlab('Month')
        + ylab('USD')
    )
    plot_file = ggsave(plot, 'plot2.html')

    with open(plot_file) as file:
        plot_html = file.read()

    return plot_html


# Question 2
@app.route('/get_high_low_diff')
def get_high_low_diff():
    # read the csv and convert the timestamp to datetime
    csv_path = 'weekly_adjusted_IBM.csv'
    df = pd.read_csv(csv_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['year'] = df['timestamp'].dt.year
    df["high_low_diff"] = df["high"] - df["low"]

    df_grouped = df.groupby('year').agg({'high_low_diff': 'mean'}).reset_index()
    plot = (
        ggplot(df_grouped, aes(x='year', y='high_low_diff')) 
        + geom_line() 
        + ggtitle('Average Weekly High-Low difference', subtitle='The most stable years being 2004-2006') 
        + xlab('Year') 
        + ylab('USD')
        )
    plot_file = ggsave(plot, 'plot3.html')

    with open(plot_file) as file:
        plot_html = file.read()

    return plot_html
    

# Question 3
@app.route('/greatest_month_change/<input>')
def greatest_month_change(input):
    data = get_monthly_change(input)
    return data


def get_monthly_change(target):
     # read the csv and create the year column
    csv_path = 'weekly_adjusted_IBM.csv'
    df = pd.read_csv(csv_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['month'] = df['timestamp'].dt.month
    df['year'] = df['timestamp'].dt.year
    # Group the data by year and calculate the change in month
    df_grouped = df.groupby(['month', 'year']).agg({'adjusted close': 'mean'}).reset_index()
    df_grouped['change'] = df_grouped['adjusted close'].pct_change()

    if target == 'min':
        least_growth = df_grouped.loc[df_grouped['change'].idxmin()]
        return least_growth.to_string()
    elif target == 'max':
        most_growth = df_grouped.loc[df_grouped['change'].idxmax()]
        return most_growth.to_string()
    else:
        return 'Invalid target'
   


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, use_reloader=False)