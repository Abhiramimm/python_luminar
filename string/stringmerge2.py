string1=input("enter string1:")
string2=input("enter string2:")
s1_length=len(string1)
s2_length=len(string2)#length=min(len(string1),len(string2))

# print(s1_length,s2_length)

output=""

sm_length= s1_length if s1_length<s2_length else s2_length

for i in range(0,sm_length):
    output+=string1[i]+string2[i]

rem=string1[s2_length:] if s1_length>s2_length else string2[s1_length:]  #string1[sm_length:]
output+=rem
print(output)
