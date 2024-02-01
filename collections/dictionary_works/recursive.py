text="goodmorning"

set_text=set(text)

wc={}

for ch in set_text:
    wc[ch]=text.count(ch)
print(wc)

#method 2
wc={ch:text.count(ch) for ch in set(text)}
print(wc)


