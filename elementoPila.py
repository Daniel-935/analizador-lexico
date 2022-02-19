
class elementoPila:

    def __init__(self,v):

        self.valor = v

    def printValor(self):

        print(self.valor)

    def returnValor(self):

        return self.valor

class terminal(elementoPila):
    pass

class noTerminal(elementoPila):
    pass

class estado(elementoPila):
    pass