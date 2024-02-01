lst=[2,2,2,2,2,2,3,4,4,4,5,5,5,5]
num_count={num:lst.count(num) for num in set(lst)}
# print(max(num_count.values()))

for k,v in num_count.items():
    if max(num_count.values())==v:
        print(k)


# method 2

def get_common(lst):
    return max(set(lst),key=lst.count)

lst=[2,2,2,2,2,2,3,4,4,4,5,5,5,5]
print(get_common(lst))













