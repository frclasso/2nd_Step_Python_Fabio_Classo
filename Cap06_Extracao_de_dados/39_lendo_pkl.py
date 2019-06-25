import pickle

with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

print(d)