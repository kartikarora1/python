n=input();
a=n[:1]
b=n[-1]
x=int(a)
y=int(b)
brr=[]
for i in range(0,x):
    arr=[]
    for j in range(0,y):
        arr.append(i*j);
    brr.append(arr)
print(brr)