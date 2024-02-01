from re import fullmatch
year="1999"   #1899 1999....2024
# rule="(18[0-9]{2}|19[0-9]{2}|20[0-9]{2})"
rule="(18|19)[0-9]{2}|20[01][0-9]|202[0-4]"

matcher=fullmatch(rule,year)
print("invalid" if matcher==None else "valid")