X = [[2,7,3],
    [9 ,6,6],
    [3 ,5,1]]

Y = [[5,8,1,2],
    [4,7,8,0],
    [4,5,6,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)