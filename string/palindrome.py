num=int(input("enter number:"))

while(True):
    if num!=0:
        original=num
    else:
        num=original
    result=""
    while(num!=0):
        digit=num%10
        result=result+str(digit)
        num=num//10
    if original==int(result):
        print(original,"palindromic number")
        break
    original+=1

