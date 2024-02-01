word="hello"

result=""   #null string
for i in range(4,-1,-1):
    result=result+word[i]  #string concatenate
print(result)

print("pallindrome" if result==word else "not palindrome")


#-------------------------------------------------------------------------or 

word="malayalam"

length=len(word)-1

result=""
for i in range(length,-1,-1):
    result=result+word[i]
print(result)