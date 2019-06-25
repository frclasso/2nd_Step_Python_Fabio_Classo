import pandas as pd

cars = pd.read_csv('cars_data.csv', index_col=0)

# print(cars.head(2))
# print()
# iteracao
# for i, row in cars.iterrows():
#     print(i + ' => ' + str(row['car_per_cap']))

# Adicionar uma coluna
for i, row in cars.iterrows():
    cars.loc[i, "name_length"] = len(row['countries'])
#print(cars.head())

# Adcionando coluna COUNTRIES
# for i, row in cars.iterrows():
#     cars.loc[i, "COUNTRIES"] = row['countries'].upper()
# print(cars.head())

cars['COUNTRIES'] = cars['countries'].apply(str.upper)
print(cars)
cars.to_csv('cars_data_modificado.csv')