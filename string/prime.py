num=int(input("enter number:"))#6
next_num=num+1    #next_num=6+1=7
while(True):
    

    for i in range(2,next_num):#(2,7)
        if next_num%i==0:  #7%2==0 false
            next_num+=1
            
        else:
            break
    print("next prime number is:", next_num)#7
    
        


