import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.metrics import mean_squared_error

inflation = pd.read_csv('E:\BJ\data sets\Data\WLD_RTFP_country_2023-07-31.csv')

inflation_numeric = inflation.drop(['country', 'ISO3', 'date'], axis=1)

sns.heatmap(inflation_numeric.corr(), cmap='crest', linewidth=.5, annot=True, square=True)
plt.show()


mode_open = inflation['Open'].mode().iloc[0]
inflation['Open'] = inflation['Open'].fillna(value=mode_open)

mode_close = inflation['Close'].mode().iloc[0]
inflation['Close'] = inflation['Close'].fillna(value=mode_close)

mode_high = inflation['High'].mode().iloc[0]
inflation['High'] = inflation['High'].fillna(value=mode_high)

mode_low = inflation['Low'].mode().iloc[0]
inflation['Low'] = inflation['Low'].fillna(value=mode_low)

inflation['date'] = pd.to_datetime(inflation['date'])

inflation.set_index('date', inplace=True)


inflation = inflation.dropna(axis=0)


plt.figure(figsize=(10, 6))
plt.plot(inflation['Close'], label='Close Value', color='blue')
plt.plot(inflation['High'], label='High Value', color='red')
plt.plot(inflation['Low'], label='Low Value', color='green')
plt.plot(inflation['Open'], label='Open Value', color='purple')
plt.title('Time Series Plot of Close Price')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()

unique_countries = inflation['country'].unique()
for country in unique_countries:
    country_data = inflation[inflation['country'] == country]
    
    plt.figure(figsize=(10, 6))
    plt.plot(country_data['Open'], label='Open Price', color='red')
    plt.plot(country_data['High'], label='High Price', color='green')
    plt.plot(country_data['Low'], label='Low Price', color='blue')
    plt.plot(country_data['Close'], label='Close Price', color='black')
    
    plt.title(f'Time Series Plot of Price Variations - {country}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    
    for country in unique_countries:
        country_data = inflation[inflation['country'] == country]
        
        plt.figure(figsize=(10, 6))
        plt.plot(country_data['Open'], label='Open Price', color='red')
        plt.plot(country_data['High'], label='High Price', color='green')
        plt.plot(country_data['Low'], label='Low Price', color='blue')
        plt.plot(country_data['Close'], label='Close Price', color='black')
        
        plt.title(f'Time Series Plot of Price Variations - {country}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)
        plt.show()
        
        plt.figure(figsize=(10,6))
        plt.plot(country_data['Inflation'], label='Inflation', color='red')
        
        plt.title(f'Time Series Plot of Inflation Variations - {country}')
        plt.xlabel('Date')
        plt.ylabel('Inflation')
        plt.legend()
        plt.grid(True)
        plt.show()
    plt.figure(figsize=(10,6))
    plt.plot(country_data['Inflation'], label='Inflation', color='red')
    
    plt.title(f'Time Series Plot of Inflation Variations - {country}')
    plt.xlabel('Date')
    plt.ylabel('Inflation')
    plt.legend()
    plt.grid(True)
    plt.show()
