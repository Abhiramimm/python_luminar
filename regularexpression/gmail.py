from re import*
gmail_id="qwer@gmail.com"

rule="[a-z]{4}(@gmail.com)"
matcher=fullmatch(rule,gmail_id)
print("invalid" if matcher==None else "valid")