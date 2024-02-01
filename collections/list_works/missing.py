arr=[5,1,4,3]
arr.sort()
left=0

while(left<len(arr)):
    right=left+1
    r_element=arr[right]
    l_element=arr[left]
    if r_element-l_element!=1:
        print(l_element+1,"is missing")
        break
    else:
        left+=1

else:
    print(r_element+1,"is missing")
