from re import*
vehicle_num="KL-09-QW-1234"
# rule="(KL)\d{2}[A-Z]{1,2}\d{4}"
rule="(KL)[-]?\d{2}[-]?[A-Z]{1,2}[-]?\d{4}"

matcher=fullmatch(rule,vehicle_num)
print("invalid" if matcher==None else "valid")