# logical operator


year=int(input("Enter  year:"))
result=year%100==0 and year%400==0
print(result)


#print true if year is not a century year and that is / 4

year=int(input("Enter  year:"))

result=year%100!=0 and year%4==0

print(result)