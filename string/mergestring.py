string1="ABC"
string2="PQRST"

length=len(string1)

output=""

for i in range(0,length):
    # print(string1[i],string2[i])
    output+=string1[i]+string2[i]
rem=string2[length:]      #rem=remaining from string2
output+=rem
print(output)