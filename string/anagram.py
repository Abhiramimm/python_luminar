source_word="listen"
target_word="silent"

# source_word="parrot"
# target_word="carrot"

srt_source_word=sorted(source_word)
srt_target_word=sorted(target_word)
print(srt_source_word)
print(srt_target_word)

if srt_source_word==srt_target_word:
    print("anagram")
else:
    print("not")