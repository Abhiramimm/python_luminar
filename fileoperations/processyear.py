base_path="C:\\Users\\Admin\\Desktop\mypython\\fileoperations\\"
years_path=base_path+"years.txt"
century_year_path=base_path+"century_years.txt"
leap_year_path=base_path+"leap_years.txt"

years_ref=open(years_path,"r")
century_ref=open(century_year_path,"w")
leap_ref=open(leap_year_path,"w")

for line in years_ref:
    year=int(line.strip("\n"))

    if year%100==0:
        century_ref.write(str(year)+"\n")
    if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
        leap_ref.write(str(year)+"\n")
        