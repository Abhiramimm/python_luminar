# print first recursive character(repeated)
text="ABBACD"
wc={}

for ch in text:
    if ch not in wc:
        wc[ch]=1
    else:
        print(ch,"is first recursive character")
        break

