from re import*
pan_num="AFZPK7190K"

rule="[A-Z]{3}[PCAFHT][A-Z]{1}\d{4}[A-Z]{1}"
matcher=fullmatch(rule,pan_num)
print("invalid" if matcher==None else "valid")
