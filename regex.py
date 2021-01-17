import re
string = input()

uppercase = re.findall(r"[A-Z]", string) 
lowercase = re.findall(r"[a-z]", string) 
numerical = re.findall(r"[0-9]", string) 
special = re.findall(r"[, .!?]", string) 
  
print("Total uppercase characters is", len(uppercase)) 
print("Total lowercase characters is", len(lowercase)) 
print("Total numerical characters is", len(numerical)) 
print("Total special characters is", len(special)) 