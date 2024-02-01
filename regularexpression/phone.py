from re import fullmatch
phone_num="6282953492"

rule="(\+91)?[0-9]{10}"
matcher=fullmatch(rule,phone_num)
print("invalid" if matcher==None else "valid")