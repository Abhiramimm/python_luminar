list=[100,200,300,150]
# list=[56,58,77,58,60]
list.sort()
largest=0 
sec_largest=0
for num in list:  #56     60
    if num>largest: #56>0  58>56  77>58 60>77 
        sec_largest=largest  #0 56 58
        largest=num  #56  58  77
    # elif num>sec_largest and num!=largest:   #60>58 60!=77
    #     sec_largest=num #60 
print(sec_largest)
print(largest)



    