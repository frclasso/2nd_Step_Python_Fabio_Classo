
import pandas as pd

df = pd.read_csv('tweets.csv', index_col=0)

# print(df['created_at'])
hora = df['created_at']

hora_certa = [entry[11:19] for entry in hora]

print('Hora')
for t in hora_certa:
    print(t)
