arr=[3,5,2,7,9,12,1,4]
element=int(input("enter element to search:"))

arr.sort()
left=0
right=len(arr)-1
while(left<=right):
    mid=(left+right)//2

    if element==arr[mid]:
        print("element found")
        break
    
    elif element>arr[mid]:
        left=mid+1
    elif element<arr[mid]:
        right=mid-1
else:
    print("element not found")
