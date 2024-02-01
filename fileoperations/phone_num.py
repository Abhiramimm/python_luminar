path="C:\\Users\\Admin\\Desktop\\mypython\\fileoperations\\phone_num.txt"

fw=open(path,"w")
phone_numbers=["8967467823","7967123456","6234567890","7567xxx678"]
# write valid phone numbers into phone_num.txt


for ph in phone_numbers:
    if len(ph)==10 and ph.isdigit():
        fw.write(ph+"\n")