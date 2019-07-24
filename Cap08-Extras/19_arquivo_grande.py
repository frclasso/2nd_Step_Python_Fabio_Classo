

import pandas as pd

data = pd.read_csv('Accidents7904.csv', low_memory=False)

#print(data.head())
# for row in data:
#     print(row)
#
# eventos = list(zip(data['Accident_Index'], data['Number_of_Casualties'],
#                    data['Date']))
#
# for e in eventos:
#     print(e)

print(data.shape())