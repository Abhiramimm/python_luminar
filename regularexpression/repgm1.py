from re import *
text="fat cat tom run very fast to catch"
pattern="at"
count=0
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())
    count+=1
print(f"total occurance of {pattern}:",count)
