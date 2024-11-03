#data Science project
#%%
from lets_plot import *
import pandas as pd
import numpy as np
LetsPlot.setup_html()

file_path = "weekly_adjusted_IBM.csv"
df = pd.read_csv(file_path)

print(df.head())

#%%

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])
plot = (
    ggplot(df, aes(x='timestamp', y='adjusted close')) 
    + geom_line()
    + ggtitle('IBM stock price')
    + xlab('Date')
    + ylab('USD')
)
plot.show()
# %%
# Save the plot to a file
path_to_plot = ggsave(plot, 'plot.html')
# %%
print(len(df['timestamp'].unique()))
# %%
# extracting the year from the timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['year'] = df['timestamp'].dt.year
print(df.head())
# %%
# Group the data by year and calculate the average adjusted close price
df_grouped = df.groupby('year').agg({'adjusted close': 'mean'}).reset_index()
print(df_grouped.head())
# %%
# Create a plot
plot = (
    ggplot(df_grouped, aes(x='year', y='adjusted close')) 
    + geom_line()
    + ggtitle('IBM stock price')
    + xlab('Year')
    + ylab('USD')
)
plot.show()
# %%
# See which year had the most dramatic change in stock price
df_grouped['change'] = df_grouped['adjusted close'].pct_change()
print(df_grouped.head())
# %%
most_dramatic_year = df_grouped.loc[df_grouped['change'].idxmax()]
print(most_dramatic_year)
# %%
least_dramatic_year = df_grouped.loc[df_grouped['change'].idxmin()]
print(least_dramatic_year)
# %%
# calculate the average adjusted close price for each month
df['month'] = df['timestamp'].dt.month
df_grouped = df.groupby('month').agg({'adjusted close': 'mean'}).reset_index()
print(df_grouped.head())
# %%
# Create a plot
plot = (
    ggplot(df_grouped, aes(x='month', y='adjusted close')) 
    + geom_line()
    + ggtitle('IBM stock price')
    + xlab('Month')
    + ylab('USD')
)
plot.show()
# %%
df['year'] = df['timestamp'].dt.year
df_year_minmax = df.groupby('year').agg({'high': 'max'}, {'low': 'min'}).reset_index()
print(df_year_minmax.head())

## This chart shows that the highest months are august through october
## but that the lowest months are november through january
# %%
# calculate the average high low difference for each week
df['high_low_diff'] = df['high'] - df['low']
# group the data by year and average the high low difference
df_grouped = df.groupby('year').agg({'high_low_diff': 'mean'}).reset_index()
plot = (ggplot(df_grouped, aes(x='year', y='high_low_diff')) + geom_line() + ggtitle('High low difference') + xlab('Year') + ylab('USD'))
plot.show()
## the most stable year was 2006, with the least variance in the high and low prices
## the highest was 2000, with the most variance in the high and low prices with an average of 10 USD difference each week