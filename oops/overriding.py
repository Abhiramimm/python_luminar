class GrandParent:
    def m1(self):
        print("inside grandparent method m1")

class Parent:
    def m1(self):
        print("inside parent method m1")

class Child(Parent,GrandParent):
    pass

ch=Child()
ch.m1()



