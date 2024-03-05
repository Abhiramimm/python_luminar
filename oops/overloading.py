# method overloading
class Operations:

    def add(self,*args):
        print(sum(args))


obj=Operations()
obj.add(10,20)
obj.add(10,20,30)