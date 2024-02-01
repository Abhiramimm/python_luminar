num1=int(input("enter num1:"))
num2=int(input("enter num2:"))

largest_num=max(num1,num2)
# product=num1*num2

while(True):  #while(product):
    if largest_num%num1==0 and largest_num%num2==0:
        lcm=largest_num
        break
    largest_num+=1
print(lcm)