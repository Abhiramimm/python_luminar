# decorator

class Emp:
    company:str

    def __init__(self):
        self.company="luminar"
    
    @property
    def get_company_name(self):
        return self.company
    
obj=Emp()
print(obj.get_company_name) 