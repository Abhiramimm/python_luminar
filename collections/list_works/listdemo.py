expenses=[15000,20000,16000,17000,12000]

# print(expenses)
# print(expenses[1])

# update march month expense as 18000

expenses[2]=18000
print(expenses)

# for i in range(0,len(expenses)):
#     print(expenses[i])


# for obj in expenses:
#     print(obj)

for obj in expenses:
    if obj>19000:
        print(obj)

# for obj in expenses:
#     if obj>=15000 and obj<=18000:
#         print(obj)

# for obj in expenses:
#     if obj in range(15000,18000):
#         print(obj)
total=0
for obj in expenses:
    total+=obj
print(total)

total=sum(expenses)
print(total)    
print(max(expenses))

costly=max(expenses)
print(costly)

cheapest=min(expenses)
print(cheapest)
    
