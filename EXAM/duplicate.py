text="aabcc"
lst=[]

for ch in text:
    if ch not in lst:
        lst.append(ch)
print(lst)