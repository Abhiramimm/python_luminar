# arr1=[1,2,3,4,5]
# arr2=[3,4,5,6]
# sum=0
# for i in arr1:
#     for j in arr2:
#         if i==j:
#             sum=sum+i
            # print(i)
# print(sum)

arr1=[1,2,3,4,5]
arr2=[3,4,5,6]            
def common_sum(arr1,arr2):
    sum=0
    for num in arr2:
        if num in arr1:
            sum+=num
    return sum
print(common_sum(arr1,arr2))


