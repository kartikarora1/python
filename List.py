#making a new list from previous list which contains squares of previous list


list=[]
list1=[]
n=int(input())
for i in range(0,n):
    num=int(input())
    list.append(num)
    list1.append(num*num)
print(list)
print(list1)