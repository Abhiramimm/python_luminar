num=121
original=num
result=" " #intialize result as string, result="121"
while(num!=0):
    digit=num%10
    result=result+str(digit)
    num=num//10
print(result)#type=string
if original==int(result):
    print("palindrome")
else:
    print("not palindrome")