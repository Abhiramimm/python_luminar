from re import fullmatch
path="C:\\Users\\Admin\\Desktop\\mypython\\regexpro\\tcodes.txt"
f=open(path,"r",encoding="UTF-8")
rule="[0-9]{3}[/][0-9]{2}[/](R)[0-9]{2}[/][0-9]{2}[a-z]{1}"
for line in f:
    tyre_code=line.rstrip("\n")
    matcher=fullmatch(rule,tyre_code)
    if matcher!=None:
        print(tyre_code)