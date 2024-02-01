# pre defined characters
from re import*
text="abcK4g h$7dg"
# pattern="\d"                 #check for all digits [0-9]
# pattern="\D"                 #excluding digits [^0-9]
# pattern="\w"                 #check for all alphanumeric [a-zA-Z0-9]
# pattern="\W"                 #check all special characters [^a-zA-Z0-9]
# pattern="\s"                 #check space
pattern="\s"                   # exclude space

matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())




