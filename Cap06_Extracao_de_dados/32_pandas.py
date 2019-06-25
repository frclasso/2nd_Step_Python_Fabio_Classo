

import pandas as pd

names = ['Unitesd States',
         'Autralia',
         'Japan',
         'India',
         'Russia',
         'Marroco',
         'Egypt']

dr = [True, False, False, False, True, True, True]
cpc = [809,731,588,18,200,70,45]

myDict = {'countries':names, 'drives_right':dr, 'car_per_cap':cpc}


# DataFrame
cars = pd.DataFrame(myDict)

#print(cars)
# cars.to_csv('cars_data.csv')
# cars.to_excel('cars_data.xlsx')

row_labels = ['US', 'AUS', 'JAP','IN', 'RU', 'MOR', 'EG']

cars.index = row_labels
print(cars)
cars.to_csv('cars_data.csv')