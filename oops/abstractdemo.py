from abc import ABC,abstractmethod
# ABC --> AbstractBaseClass

class Car(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Fronx(Car):
    def start(self):
        print("fronx start method")
    
    def accelerate(self):
        print("fronx accelerate method")

    def stop(self):
        print("fronx stop method")

fx=Fronx()
fx.start()
fx.accelerate()
fx.stop()
