def is_prime(num):
    for i in range(2,num):
        if(num % i == 0):
            return False
        else:
            return True
print(is_prime(9))

def is_leapyear(year):
      if(year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
        return True
      else:
          return False
# print(is_leapyear(2024))