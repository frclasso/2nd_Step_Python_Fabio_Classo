M = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]

print(list(map(sum,M)))

# creating a set using comprehension syntax
print({sum(row) for row in M}) # creates a set of row sums

# creating a dictionary using comprehension syntax
print({i : sum(M[i])for i in range(3)}) # creates key/value table of row sums