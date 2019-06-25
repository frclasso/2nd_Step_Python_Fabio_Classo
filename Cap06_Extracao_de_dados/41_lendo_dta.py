import pandas as pd

df = pd.read_stata('disarea.dta')
print(df.head())
print(df.info())