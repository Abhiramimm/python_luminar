prev=0
current=1

print(prev,current)
for i in range(0,10):
    next=prev+current
    print(next)
    prev=current
    current=next