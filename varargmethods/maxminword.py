# print longest word in a text

text="longest word"
words=text.split(" ")
# print(words)

def get_length(words):
    return len(words)

# longest_word=max(words,key=get_length)
# print(longest_word)

def get_max_min_word(text,is_max=True):
    words=text.split(" ")
    if is_max==True:
        return max(words,key=get_length)
    else:
        return min(words,key=get_length)

print(get_max_min_word(text))
print(get_max_min_word(text,is_max=False))

        


