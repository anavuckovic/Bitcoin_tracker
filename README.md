Bitcoin Risk and Sharpe Ratio Analysis
This project was created as part of the Python for Finance certificate on SoloLearn in July 2022. 
The goal of this project is to analyze Bitcoin's (BTC) historical price data, calculate daily returns, assess risk (volatility), and compute the Sharpe ratio.

The code uses data from Yahoo Finance (via the yfinance library) to gather Bitcoin's price history and then performs various financial calculations. 
The results are visualized using Matplotlib.

Key Features:
  Data Retrieval: Fetches historical Bitcoin price data using yfinance.
  Risk Calculation: Computes annual volatility based on daily price changes.
  Sharpe Ratio: Calculates the Sharpe ratio to measure risk-adjusted return.
  Visualization: Plots the Bitcoin portfolio growth over the selected period.
  
Requirements:
  Python 3.x
  numpy for numerical computations
  numpy_financial for financial functions
  matplotlib for plotting data
  yfinance for fetching financial data

Installation:
To get started with this project, make sure you have the following libraries installed. You can install them via pip:
  pip install numpy numpy-financial matplotlib yfinance

Code Explanation:
  Data Import: The code uses the yfinance library to fetch the historical price data of Bitcoin (BTC-USD) for the last year.
  Risk (Volatility) Calculation: The standard deviation of daily percentage changes in Bitcoin's price is calculated to determine annual volatility, 
  which is then scaled by the square root of 252 (trading days in a year).
  Sharpe Ratio Calculation: This helps assess the risk-adjusted return of Bitcoin.
  Portfolio Simulation: The code simulates an investment of 1000 units of Bitcoin at the starting price, tracks its growth, and plots the portfolio value over time.
  Visualization: A plot of the Bitcoin portfolio's value is generated and saved as plot.png.

Example Output:
  Risk (Volatility): The code will print out the calculated annual volatility (in percentage terms) of Bitcoin.
  Sharpe Ratio: The Sharpe ratio is calculated and printed, which measures the risk-adjusted return of the Bitcoin investment.
  Plot: A graph of the Bitcoin portfolio value over time is generated and saved as a PNG image.

Example Usage:
  To run the code, simply execute the script in a Python environment. The program will fetch the latest data, calculate the required metrics, and generate the portfolio plot.

License:
This project is for educational purposes and follows the MIT License. Feel free to fork and modify it as you wish.

