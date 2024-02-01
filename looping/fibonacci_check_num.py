prev=0
current=1
limit=30
num=45
is_fibo=False


for i in range(1,num+1):
    next=prev+current
    prev=current
    current=next
    if(next==num):
        is_fibo=True
        break
print(is_fibo)
    
    
    
    