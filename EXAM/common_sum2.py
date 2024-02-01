arr1=[1,2,3,4,5]
arr2=[3,4,5,6]

def common_sum(arr1,arr2):
    wc={num:arr1.count(num) for num in set(arr2)}
    total=sum([k for k,v in wc.items() if v>0])
    return total
print(common_sum(arr1,arr2))
