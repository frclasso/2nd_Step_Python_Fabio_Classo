M = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]

diag = [M[i][i] for i in [0,1,2]] # Collect  a diagonal from matrix
print(diag)

doubles = [x * 2 for x in 'spam']
print(doubles)

print([[x**2, x**3]for x in range(4)])
#multiplas condicoes
print([[x, x/2, x*2] for x in range(-6,7,2) if x > 0])