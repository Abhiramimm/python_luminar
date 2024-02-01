loan_amount=200000
intrest_rate=9
tenure=20

# 20years=20*12=240
n=240

monthly_intrest_rate=intrest_rate/(12*100)
# print(monthly_intrest_rate)

emi = loan_amount*monthly_intrest_rate*((1+monthly_intrest_rate)**n)/((1+monthly_intrest_rate)**n - 1)
print("Monthly EMI = ", emi)

total_interest=(emi*n)-loan_amount
print("Total interest = ", total_interest)

total_payment=loan_amount+total_interest
print("Total payment = ", total_payment)


