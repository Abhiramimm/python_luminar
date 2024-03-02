class Student:
    name:str
    course:str
    degree:str
    
    # def set_student(self,name,course,degree):
    #     self.name=name
    #     self.course=course
    #     self.degree=degree

    def __init__(self,name,course,degree):
        self.name=name
        self.course=course
        self.degree=degree
    def display(self):
        print(self.name,self.course,self.degree)
# obj1=Student()
# obj1.set_student("JaneDoe","Django","MCA")

obj1=Student("JaneDoe","Django","MCA")
obj1.display()

