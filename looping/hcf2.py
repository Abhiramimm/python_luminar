# num1=50
# num2=10
# i=1
# while(i<=num2):
#   if (num1%i==0):
#     print(i)
#   elif (num2%i==0):
#     print(i)
#   i=i+1

num1=int(input("enter num1:"))
num2=int(input("enter num2:"))

sm_num=num1 if num1<num2 else num2 
i=1

while(i<=sm_num):
    if(num1%i==0) and (num2%i==0):
        hcf=i
    i=i+1
print(f"hcf of {num1},{num2} = {hcf}")