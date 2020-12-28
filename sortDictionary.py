dict1 = {'gfg': [7, 6, 3],  
             'is': [2, 10, 3],  
             'best': [19, 4]} 
  
 
print("The original dictionary is : " + str(dict1)) 
  
res = dict1() 
for key in sorted(dict1): 
    res[key] = sorted(dict1[key]) 
  
print("The sorted dictionary : " + str(res))  