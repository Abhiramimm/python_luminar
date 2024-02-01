from json import load

f=open("C:\\Users\\Admin\\Desktop\\mypython\\json_works\\processingEmployees\\data.json","r")

employees=load(f)
# print(employees)

# q1 print no.of employees
print(len(employees))

# print all employee name
employee_names=[emp.get("name") for emp in employees]
# print(employee_names)

# q3 print employee names working as qa
for e in employees:
    if e.get("department")=="qa":
        print(e.get("name"))

dept_filter=[e.get("name") for e in employees if e.get("department")=="qa"]
print(dept_filter)

# q4 location ekm employee name

location_filter=[e.get("name") for e in employees if e.get("location")=="ekm"]
print(location_filter)