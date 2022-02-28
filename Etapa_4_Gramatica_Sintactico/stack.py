import elementoPila


class stack:

    def __init__(self):
        
        self.stack = []

    def push(self,e):

        self.stack.append(e)

    def top(self):

        return self.stack[-1]

    def pop(self):

        return self.stack.pop()

    def stackSize(self):

        return len(self.stack)

    def isEmpty(self):

        if len(self.stack)==0:

            return True
        return False

    def limpiar(self):

        self.stack = []

    def printStack(self):

        for i in self.stack:

            print(i.printValor())
