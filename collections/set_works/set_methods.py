st={10,20,30,40}
#add
# st.add(50)
# print(st)

#pop()
# st.pop()
# print(st)

#remove
# st.remove(40)
# print(st)

#discard

st.discard(400)  #if value not present return none 
print(st)

st1={10,20,30,40}
st2={30,40,50,60}
union_set=st1.union(st2)
print(union_set)

intersection_set=st1.intersection(st2)
print(intersection_set)

difference_set=st1.difference(st2)
print(difference_set)


colors={"red","green","blue"}
new_set={"cyan","purple","brown"}

colors.update(new_set)
print(colors)