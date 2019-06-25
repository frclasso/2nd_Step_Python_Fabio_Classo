import numpy as np

data = np.recfromcsv('Titanic_2.csv',
                     delimiter=',',
                     names=True,
                     dtype=None,
                     encoding='utf-8')

print(data[:5])  # equivalente ao .head()