from json import load

f=open("C:\\Users\\Admin\\Desktop\\mypython\\json_works\\processingjson\\students.json","r")

data=load(f)
# for dictionary in data:
#     print(dictionary.get("name"))
#     print(dictionary.get("course"))

for dictionary in data:
    if dictionary.get("place")=="thrissur":
        print(dictionary.get("name"))

place_filter=[dictionary.get("name") for dictionary in data if dictionary.get("place")=="thrissur"]
# print(place_filter)

# print all courses
        
wc=[dictionary.get("course") for dictionary in data]
# print(set(wc))
st=set()
for dictionary in data:
    st.add(dictionary.get("course"))  #course=dictionary.get
print(st)


