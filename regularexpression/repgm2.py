from re import*
text="Pam has a cat. The cat is fat. The fat cat is black. Black fat cat sat in the jam. Pam has a rag bag. In the bag went Black Fat Cat. Dad and Pam ran with Black Fat Cat to the tap."
pattern="am"
count=0
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())
    count+=1
print(f"total occurance of {pattern}:",count)