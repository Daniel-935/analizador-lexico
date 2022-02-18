
class elementoPila:

    def __init__(self):

        self.valor = ""

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