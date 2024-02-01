text="fat cat mat cat fat cat"

wc={}

words=text.split(" ")

for w in words:
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1
print(wc)