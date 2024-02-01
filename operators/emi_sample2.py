loan_amount=200000
interest_rate=9
tenure=20

# EMI=p*i*(1+i)^n/(1+i)^n-1

p=loan_amount

r=interest_rate/12
i=r/100
n=tenure*12

one_pluse_power=(1+i)**n

emi=(p*i*one_pluse_power)/(one_pluse_power-1)

print(f"emi amount={emi}")