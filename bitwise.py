def bitwise(a, b):
    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a
print(bitwise(2, 10))
print(bitwise(-20, 10))
print(bitwise(-10, -20))