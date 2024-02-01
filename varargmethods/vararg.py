def add_numbers(*args):
    # print(args)
    return sum(args)
print(add_numbers(10,20,30))

def display_student(**kwargs):
    print(kwargs.get("name"))

display_student(id="400",name="Vijay",total="550",course="mca")



def display_mobile_details(**kwargs):
    print(kwargs.get("name"))

display_mobile_details(name="redmiote13pro",brand="redmi",price=23000)


