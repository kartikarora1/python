import re 

string = input()
print ("String Before : ",string) 
res = re.sub('[\W_]+', '', string) 
print ("String After", res) 