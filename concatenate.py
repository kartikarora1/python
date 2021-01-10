s=input()
n=input()
a=len(s)
b=len(n)
for x in range(a):
    if s[x] not in n:
        print(s[x],end="")
for x in range(b):
    if n[x] not in s:
        print(n[x],end="")