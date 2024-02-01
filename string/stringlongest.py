text="this is a goodmorning msg"

#print longest word in string

words=text.split(" ")

def get_len(w):
    return len(w)

min_word=min(words,key=get_len)
# print(min_word)

max_word=max(words,key=get_len)
# print(max_word)

# ------------------------------------------------------------------------------------

print(max(words,key=lambda w:len(w)))

srt_words=sorted(words,key=get_len)#ascending order
print(srt_words)

srt_words=sorted(words,key=get_len, reverse=True)#descending order
print(srt_words)

