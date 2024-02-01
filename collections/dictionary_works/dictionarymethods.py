course={
    "name":"django",
    "language": "python",
    "duration":7,
    "fees":50000,
    "faculty":"shyam"
}

#keys()

for k in course.keys():
    print(k)

#values()
    
    for v in course.values():
        print(v)

#items() =>k,v
        
for k,v in course.items():
    print(k,v)

#get(key)
print(course.get("name"))

#update()
course.update({"duration":8,"fees":60000})
print(course)

course.update({"duration":10})
print(course)

#pop(key)
course.pop("faculty")
print(course)

