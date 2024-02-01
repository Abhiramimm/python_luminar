years=[]
century_years=[]
non_century_years=[]  
leap_years=[]

for y in range(1800,2025):
    years.append(y)
# print("all years",years)


for y in years:
    if y%100==0:
        century_years.append(years)
    else:
        non_century_years.append(years)
# print("century years:",century_years)
# print("non century years:",non_century_years)
        
for y in years:
    if(y%100==0 and  y%400==0) or (y%100!=0 and  y%4==0):
        leap_years.append(y)
print("leap years:",leap_years)
    
print("no.of leap years from 1800-2024:",len(leap_years))