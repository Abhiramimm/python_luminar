class Vehicle:
    name:str
    brand:str

    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
    
    def display_specs(self):
        print(self.name,self.brand)
    

class Car(Vehicle):
    transmission_type:str

    def __init__(self, name, brand,transmission):
        super().__init__(name, brand)   #calling parent class constructor method
        self.transmission_type=transmission

    def display_specs(self):
        super().display_specs()   #calling parent class display method
        print(self.transmission_type)

obj1=Car("fronx","nexa","manuel")
obj1.display_specs()


        