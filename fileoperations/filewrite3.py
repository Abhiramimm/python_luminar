vehicle_numbers=["KL-08-BN-2345","KA-08-HK-5678","TN-05-BN-8907","KL-08-BN-2345","TN-05-BN-8907"]

path="C:\\Users\\Admin\\Desktop\\mypython\\fileoperations\\vehicle_numbers.txt"

f=open(path,"w")

for number in vehicle_numbers:
    if number.startswith("KL"):
        f.write(number+"\n")