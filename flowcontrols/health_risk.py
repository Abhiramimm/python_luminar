tummy_size=int(input("enter tummy size:"))
buttock_size=int(input("enter buttock size:"))
gender=input("Enter gender:")

value=tummy_size/buttock_size
value=round(value,2)

print(value)

if(gender=="female" and value<=0.80):
    print("low")
elif(gender=="female" and value<0.85):
    print("moderate")
elif(gender=="female" and value>0.85):
    print("high")
elif(gender=="male" and value<=0.95):
    print("low")
    
elif(gender=="male" and value<1.0):
    print("moderate")
elif(gender=="male" and value>1.0):
    print("high")