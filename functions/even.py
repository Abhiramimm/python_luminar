#create a function is_even that take one parameter num  and return True if num is even else return False

def is_even(num):
    if num%2==0:
        return True
    else:
        return False
# print(is_even(8))
#  or

def is_even(num):
    return True if num%2==0 else False
# print(is_even(8))

# --------------------------------------------------------
def last_digit_max_num(n1,n2):
        last_digit_n1=n1%10
        last_digit_n2=n2%10
        return n1 if last_digit_n1>last_digit_n2 else n2
# print(last_digit_max_num(257,450))

# ---------------------------------------------------------------

def nth_power(num,exp):
     return num**exp  
# print(nth_power(10,2))     

# --------------------------------------------------------------------------------

def smart_sub(n1,n2):
    if n1>n2:
         result=n1-n2
         return result
    else:
         result=n2-n1
         return result
# print(smart_sub(8,10))

def smart_sub(n1,n2):
     return n1-n2 if n1>n2 else n2-n1
print(smart_sub(8,10))
     





    
    
    
    

    