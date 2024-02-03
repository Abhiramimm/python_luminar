from re import fullmatch
path="C:\\Users\\Admin\\Desktop\\mypython\\regexpro\\emailid.txt"
f=open(path,"r",encoding="UTF-8")
rule="[a-z][0-9a-z_]*(@gmail.com)"
for line in f:
    email_id=line.rstrip("\n")
    matcher=fullmatch(rule,email_id)
    if matcher!=None:
        print(email_id)