#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('bio_stats.csv')

#print(df.info())
print(df.head())
#print(df.tail())

#print(df['Name'])