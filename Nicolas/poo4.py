class Caneta:
    def __init__(self, marca : str, cor : str):
        self.__marca = marca;
        self.__cor = cor;
    
    def escrever(self):
        print(f"A caneta {self.marca} está escrevendo na cor {self.cor}");
    
    @property
    def marca(self):
        return self.__marca;
    
    @property
    def cor(self):
        return self.__cor;

class Escritor:
    def __init__(self, nome : str, caneta : Caneta):
        self.__nome = nome;
        self.__caneta = caneta;
    
    def escrever(self):
        print(f"O escritor {self.nome} está utlizando sua caneta.")
        self.caneta.escrever();

    @property
    def nome(self):
        return self.__nome;
    
    @property
    def caneta(self):
        return self.__caneta;

caneta = Caneta("Bic", "Vermelha");
escritor = Escritor("Machado de assis", caneta)

escritor.escrever();