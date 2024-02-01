arr=[2,3,5,4]
arr.sort()

left=0
right=len(arr)-1
sum=8
counter=0
is_present=False
while(left<right):
    left_element=arr[left]
    right_element=arr[right]
    current_sum=left_element+right_element
    if sum==current_sum:
        print("pairs",left_element,right_element)
        is_present=True
        break
    elif sum>current_sum:
        left=left+1
    elif sum<current_sum:
        right=right-1
    counter+=1
print("total no.of execution:",counter)
if is_present==False:
    print("no pair exist")
    
    