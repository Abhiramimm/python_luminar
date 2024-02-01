from re import fullmatch
month="09"
rule="(0[1-9]|1[012])"
matcher=fullmatch(rule,month)
print("invalid" if matcher==None else "valid")