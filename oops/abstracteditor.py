from abc import ABC,abstractmethod
class Editor(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class Vscode(Editor):

    def open(self):
        print("vscode open method")
    def save(self):
        print("vscode save method")
    def edit(self):
        print("vscode edit method")
    def execute(self):
        print("vscode execute method")

vs=Vscode()
vs.open()
vs.save()
vs.edit()
vs.execute()