class Produto:
    def __init__(self,nome):
        self.nome = nome
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,valor):
        self._nome = valor.upper()
        
        
p1 =Produto("oii")
print(p1.nome)
