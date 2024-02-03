from re import fullmatch
path="C:\\Users\\Admin\\Desktop\\mypython\\regexpro\\numbers.txt"
f=open(path,"r")
rule="(\+91)?\d{10}"
for line in f:
    phone_number=line.rstrip("\n")
    matcher=fullmatch(rule,phone_number)
    if matcher!=None:
        print(phone_number)