from re import*
text="abc K4gh$ 7dg"
    # 0123456789101112

# pattern="[a-z]"        #check for all lowercase alphabets
# pattern="[A-Z]"        # check for all upper case alphates

# character set
# **************
# pattern="[a-zA-Z]"       # check for all alphabets
# pattern="[0-9]"          #check for all digits
# pattern="[a-zA-Z0-9]"    #check for all alpha-numeric
# pattern="[^a-zA-Z0-9]"   #special character, exclude [^pattern]
pattern="[abc]"            # either a,b or c



matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())
