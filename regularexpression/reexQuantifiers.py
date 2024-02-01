# quantifiers (*,+,?,{})

from re import *
text="aabaaabcaaccaaa"

# pattern="a*"      # check for any no of a including zero
# pattern="a{2}"    # check for 2a  
pattern="a{2,3}"    # mininum 2, maximum 3


matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())