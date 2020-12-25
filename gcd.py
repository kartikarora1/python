# Python program to find H.C.F of two numbers

def gcd(x, y):

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i 
    return gcd

num1 = int(input()) 
num2 = int(input())

print("The H.C.F. is", gcd(num1, num2))