arr=[2,3,5,4]

sum=8
counter=0
is_present=False
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        i_element=arr[i]
        j_element=arr[j]
        current_sum=i_element+j_element
        if sum==current_sum:
            print("pairs",i_element,j_element)
            is_present=True
            break
        counter+=1
print("total no.of execution:",counter)

if is_present==False:
    print("no pair exist")