students=[

    {"rol":100,"name":"arjun","course":"django"},
    {"rol":101,"name":"biju","course":"mearn"},
    {"rol":102,"name":"cijoy","course":"testing"},
    {"rol":103,"name":"vipin","course":"django"},
    {"rol":104,"name":"tom","course":"mearn"},
    {"rol":105,"name":"jhon","course":"testing"},
    {"rol":106,"name":"nibin","course":"django"},



]

for dictionary in students:
    # print(dictionary.get("course"))
    if dictionary.get("course")=="django":
        print(dictionary.get("name"))
    