class Employee:
    emp_code:str
    name:str
    dept_name:str
    salary:int
    def set_employee(self,emp_code,name,dept_name,salary):
        self.emp_code=emp_code
        self.name=name
        self.dept_name=dept_name
        self.salary=salary
    def display(self):
        print(self.emp_code,self.name,self.dept_name,self.salary)

obj1=Employee()
obj1.set_employee("E101","JaneDoe","hr","45000")
obj1.display()

ob2=Employee()
ob2.set_employee("E102","JohnDoe","IT","40000")
ob2.display()