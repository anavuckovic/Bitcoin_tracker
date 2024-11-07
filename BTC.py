import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt
import yfinance as yf

data = yf.Ticker('BTC-USD')
x = data.history('1y')['Close']

#Daily returns
d = yf.download('BTC-USD',start = '2023-01-01')
#Percentage change
pc = d['Close'].pct_change()
#Volatility
annual = np.std(pc)*np.sqrt(252)*100
print("Risk: ",annual)
sharpe = (np.mean(pc)/np.std(pc))*np.sqrt(252)
print("Sharpe: ",sharpe)

num_of_btc = 1000/x[0]
btc = np.multiply(x,num_of_btc)
plt.plot(btc)
plt.savefig('plot.png')
