class Caneta:
    def __init__(self,marca,cor):
        self.__marca = marca
        self.__cor = cor
    @property
    def marca(self):
        return self.__marca
    @property
    def cor(self):
        return self.__cor
    def escrever(self):
        print(f'Caneta {self.marca} está escrevendo na cor {self.cor}.')
class Escritor:
    def __init__(self,nome):
        self.nome = nome
        self.caneta = None
    def escrevendo(self):
        if self.caneta is not None:
            self.caneta.escrever()
        else:
            print(f'{self.nome} não tem uma caneta para escrever.')

c1 = Caneta("Bic","Azul")
e1 = Escritor("Joao")
e1.caneta = c1
e1.escrevendo()


