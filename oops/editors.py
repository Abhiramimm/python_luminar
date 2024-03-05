# method overriding
class Editor:
    functionality_list=["open","save","edit"]

    def get_context(self):
        return self.functionality_list
    def print_functions(self):
        print(self.get_context())


class Vscode(Editor):

    def get_context(self):
        self.context=super().get_context()
        self.context.append("debug")
        self.context.append("execute")
        return self.context

ch=Vscode()
ch.print_functions()


    