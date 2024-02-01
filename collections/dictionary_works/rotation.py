lst=[1,2,3,4,5,6,7]

# k=2
# first rotation=[7,1,2,3,4,5,6]
# second rotation=[6,7,1,2,3,4,5]
k=2
for i in range(0,k):
    last_element=lst.pop()
    lst.insert(0,last_element)
print(lst)