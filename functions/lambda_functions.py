addition=lambda n1,n2:n1+n2
print(addition(100,200))

substract=lambda n1,n2:n1-n2
print((substract(200,100)))

cube=lambda n:n**3
print(cube(2))

maxTwo=lambda n1,n2:n1 if n1>n2 else n2
print(maxTwo(2,4))

is_even=lambda n:True if n%2==0 else False
print((is_even(8)))

last_digit_max=lambda n1,n2:n1 if n1%10>n2%10 else n2
print(last_digit_max(125,400))

nth_power=lambda num,exp:num**exp
print(nth_power(2,4))

is_leap_year=lambda year:True if (year%100==0 and year%400==0)| (year%100!=0 and year%4==0) else False
print(is_leap_year(2024))


smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
print(smart_sub(2,8))

# is_prime=lambda n: not any ([n%i==0])
