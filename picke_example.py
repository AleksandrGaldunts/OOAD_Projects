# import pickle
#
# # Example Python object
# data = {'key': 'value', 'number': 42}
#
# # Serializing the object to a pickle file
# with open('data.pkl', 'wb') as f:
#     pickle.dump(data, f)
#
# # Deserializing the object from the pickle file
# with open('data.pkl', 'rb') as f:
#     loaded_data = pickle.load(f)
#
# print(loaded_data)


from pandas_datareader import data, wb
import datetime

# Define the start and end dates for data retrieval
start = datetime.datetime(2023, 1, 1)
end = datetime.datetime(2023, 12, 31)

# Get stock price data from Yahoo Finance
stock_data = data.get_data_yahoo('AAPL', start, end)
print(stock_data)

# Get World Bank data
# Example: Downloading GDP data for the United States
gdp_data = wb.download(indicator='NY.GDP.MKTP.CD', country='US', start=2010, end=2020)
print(gdp_data)

