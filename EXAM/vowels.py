# text="Hello hello"
# result=text.casefold()
# vowels=["a","e","i","o","u"]
# v_count=0
# for ch in result:
#     if ch in vowels:
#         v_count+=1
# print(v_count)

def count_vowels(txt):
    count=0
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    for ch in txt:
        if ch in vowels:
            count=count+1
    return count
txt="The quick brown fox jumps over the lazy dog"
count_vowels(txt)

