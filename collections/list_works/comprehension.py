list=[1,2,3,4,5,7]
# squares=[]

# for num in list:
#     sq=num**2
#     squares.append(sq)
# print(squares)

#----------------------------------------------------
# cubes=[num**3 for num in list]
# print(cubes)

# add_five=[num+5 for num in list]
# print(add_five)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# evens=[]
# for num in list:
#     if num%2==0:
#         evens.append(num)
# print(evens)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# oods=[num for num in list if num%2!=0]
# # print(oods)
# ______________________________________________________________________________________________
lst=[1,1,1,0,1,0,0,0,0,0]
# [0,0,1,1,1,1]

counting_order=sorted(lst,key=lst.count,reverse=False)
print("counting order is:",counting_order)

# ---------------------------------------------------------------------


languages=["python","c++","c","java","javascript","typescript"]
# new_list=[]
# for lang in languages:
#     new_list.append(lang.upper())
# print(new_list)

new_list=[lang.upper() for lang in languages]
# print(new_list)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#filter names count>5

# len_filter=[lang for lang in languages if len(lang)>5]
# print(len_filter)
# --------------------------------------------------------------------
# lst=[0,1,1,1,0,0,1,0,1]

# wc={num:lst.count(num) for num in set(lst)}
# print(wc)

# .....................................................................

# lst=[2,4,6,3,1]
# maped_nums=[num+1 if num>5 else num-1 for num in lst]
# print(maped_nums)

# ......................................................................................

lst=["-","+","-","-","+","-","+","+"]

# 0,1

# map_symbols=[1 if sym=="+" else 0 for sym in lst]
# print(map_symbols)
