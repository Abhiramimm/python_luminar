#find next palindrome number
num=int(input("enter number:"))
def palindrome(num):
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
            return original
        original+=1
if num==palindrome(num):
     print(palindrome(num+1))
else:
    print(palindrome(num))

