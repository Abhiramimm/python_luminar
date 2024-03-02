class GrandParent:
    def m1(self):
        print("garnd parent m1 method")

class Parent(GrandParent):
    def m2(self):
        print("parent m2 method")

class Child(Parent):
    def m3(self):
        print("child m3 method")

ch=Child()
ch.m2()
ch.m3()