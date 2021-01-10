import re
import math
import string
s=input();
a=len(s);
if s[0]>='a' and s[0]<='z':
    print(s.title());
else:
    print(s)