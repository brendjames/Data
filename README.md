Time Series Analysis and Visualization of Inflation Data

This repository contains Python code for analyzing and visualizing time series data related to inflation using various libraries such as Pandas, NumPy, Matplotlib, Seaborn, Statsmodels, and Scikit-Learn. The code performs data cleaning, explores the dataset's correlation structure, handles missing values, and generates informative visualizations.

Overview

Inflation data is essential for economic analysis and forecasting. This project aims to provide insights into inflation trends by analyzing time series data. The key steps involved in this project are as follows:

1. Importing Libraries: We start by importing the necessary Python libraries that will be used for data analysis and visualization.

2. Loading the Data: We load the inflation data from a CSV file using Pandas. The dataset contains information about inflation, including Open, High, Low, Close prices, and more.

3. Correlation Heatmap: We create a correlation heatmap to visualize the relationships between numeric variables in the dataset. This helps us understand how different features are correlated.

4. Handling Missing Values: We address missing values in the 'Open', 'High', 'Low', and 'Close' columns by filling them with the mode of each respective column.

5. Data Preprocessing: We convert the 'date' column to a datetime format and set it as the index since we are working with time-series data. We also remove rows with missing values in the 'Inflation' column.

6. Time Series Plots: We generate time series plots to visualize the variations in 'Open', 'High', 'Low', and 'Close' prices over time. These plots provide insights into the trends and fluctuations in these variables.

7. Country-specific Analysis: We perform similar time series analysis for each unique country in the dataset. For each country, we create time series plots for 'Open', 'High', 'Low', 'Close', and 'Inflation'. This allows for a detailed examination of inflation trends for individual countries.

8. Conclusion: We conclude the analysis by summarizing the insights gained from the time series plots and visualizations.

Usage

To use this code, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have the required libraries installed (Pandas, NumPy, Matplotlib, Seaborn, Statsmodels, and Scikit-Learn).
3. Download the inflation dataset and place it in the appropriate directory https://www.kaggle.com/datasets/harshalhonde/monthly-food-price-inflation-estimates-by-country.
4. Run the Python script to perform the analysis and generate the visualizations.

Feel free to customize the code and adapt it to your specific dataset or use case.

Credits

This project was created by Brendon Kirk 