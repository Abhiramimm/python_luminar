class Book:
    title:str
    author:str
    price:int
    pages:int

    def __str__(self):
        return self.title
    
    def __init__(self,title,author,price,pages):
        self.title=title
        self.author=author
        self.price=price
        self.pages=pages

obj1=Book("randamoozham","mt",550,480)
obj2=Book("aarachar","meera",450,420)

print(obj1)
print(obj2)


