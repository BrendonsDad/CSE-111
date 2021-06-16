import pandas as pd


dataframe = pd.read_csv("w09water.csv")

meterColumn = [dataframe['meterSize'] < .8]
filteredDataframe = dataframe["meterSize"]

print(filteredDataframe)
