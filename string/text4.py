text="pneumonoultramicroscopicsilicovolcanoconiosis"

vowels=('a','e','i','o','u')
v_count=0
c_count=0
char_count=0

for ch in text:
    if ch.isalpha():
        char_count+=1
for ch in text:
    if ch in vowels:
        v_count=v_count+1
    else:
        c_count=c_count+1
    
# total_ch=v_count+c_count

print("v_count:",v_count)
print("c_count:",c_count)
print("char_count:", char_count)
# print(f"total no.of characters :{total_ch}")

    
    