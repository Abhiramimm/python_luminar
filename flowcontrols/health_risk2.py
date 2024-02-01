tummy_size=int(input("enter tummy size:"))
buttock_size=int(input("enter buttock size:"))
gender=input("Enter gender:")

value=tummy_size/buttock_size
value=round(value,2)

print(value)

if gender=="male":
    if  value<=.95:
        print("low health risk")
    elif value<=1.0:
        print("moderate health risk")
    elif value>1:
        print("high health risk")
elif gender=="female":
    if value <=.80:
        print("low health risk")
    elif value <=.85:
        print("moderate health risk")
    elif value>.85:
        print("high health risk")
   