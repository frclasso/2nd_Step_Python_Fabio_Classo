M = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]
print(M)
print(M[0])
print(M[1][2])

# comprehensions
col2 = [row[1] for row in M]
print(col2)
coladd = [row[1] + 1 for row in M]
print(coladd)
odd = [row[1] for row in M if row[1] % 2 == 0] # filter odd items
print(odd)