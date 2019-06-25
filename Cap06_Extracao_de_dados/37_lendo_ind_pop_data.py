import pandas as pd


df = pd.read_csv('ind_pop_data.csv', chunksize=10)


print(next(df))
print(next(df))