def linear(list, n, key):  
    for i in range(0, n):  
        if (list[i] == key):  
            return i  
    return -1  

list = []
p=int(input("Enter total no of elements"))
for i in range(0,p):
    x=int(input("Enter elements"))
    list.append(x)
key = input()
n = len(list)  
res = linear(list, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res)