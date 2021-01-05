X = [[1,9,3],
    [2 ,5,7],
    [6 ,6,6]]

Y = [[5,7,1],
    [9,7,3],
    [4,2,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)