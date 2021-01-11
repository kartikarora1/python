a=int(input("enter exponent"))
b=int(input("enter power"))

def power(a,b):
    if(b==0):
        return 1    
    else:
        return a*power(a,b-1)
print(power(a,b))