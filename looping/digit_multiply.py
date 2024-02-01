num=452
mul=1
while(num!=0):
    digit=num%10
    mul=mul*digit
    num=num//10
    print(mul)