from re import fullmatch
path="C:\\Users\\Admin\\Desktop\\mypython\\regexpro\\pannum.txt"
f=open(path,"r")
rule="[A-Z]{3}[PCAFHT]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}"
for line in f:
    pan_number=line.rstrip("\n")
    matcher=fullmatch(rule,pan_number)
    if matcher!=None:
        print(pan_number)