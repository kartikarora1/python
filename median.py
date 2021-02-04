x = input("First number: ")
y = input("Second number: ")
z = input("Third number: ")
print("Median: ")

if y < x and x < z:
    print(x)
elif z < x and x < y:
    print(x)
    
elif z < y and y < x:
    print(y)
elif x < y and y < z:
    print(y)
    
elif y < z and z < x:
    print(z)    
elif x < z and z < y:
    print(z)