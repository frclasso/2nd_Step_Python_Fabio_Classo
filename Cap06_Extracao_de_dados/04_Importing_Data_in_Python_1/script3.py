import pandas as pd

# Assign the filename: file
file = 'Titanic_2.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head(10))
print(df.sum(numeric_only=True))
sex = df['Sex']
female =0
male =0
for f in sex:
    if f == 'male':
        female +=1
    else: male += 1

print('Female:',female)
print('Male:',male)
