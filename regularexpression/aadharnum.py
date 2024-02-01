from re import*

aadhar_num="123456789101"

rule="[0-9]{4}[0-9]{4}[0-9]{4}"
matcher=fullmatch(rule,aadhar_num)
print("invalid" if matcher==None else "valid")