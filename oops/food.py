class Food:
    name:str
    cuisine:str
    mealtype=str

    def __init__(self,name,cuisine,mealtype):
        self.name=name
        self.cuisine=cuisine
        self.mealtype=mealtype
    def display(self):
        print(self.name,self.cuisine,self.mealtype)

obj1=Food("ghee roast","Indian","breakfast")
# obj1.set_food("ghee roast","Indian","breakfast")
obj1.display()

# obj2=Food()
# obj2.set_food("fried rice","Chinese","lunch")
# obj2.display()