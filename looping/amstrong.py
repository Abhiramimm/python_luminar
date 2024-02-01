num=input("enter a number:")

digit_count=len(num)
num=int(num)
sum=0
original=num
while(num!=0):
    digit=num%10
    exp=digit**digit_count
    sum=sum+exp
    num=num//10
# print(sum)
result=("amstrong" if original==sum else "not amstrong" )
print(result)
# if original==sum:
#     print("amstrong")
# else:
#     print("not amstrong")