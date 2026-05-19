class Cliente:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
    def insere_endereco(self,cidade,estado):
        self.enderecos.append(Endereco(cidade, estado))
    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)
    def __del__(self):
        print(f'O cliente {self.nome} foi deletado')

class Endereco:
    def __init__(self,cidade,estado):
        self.cidade = cidade
        self.estado = estado

c1 = Cliente("marcos", 30)
c1.insere_endereco("salvador","BA")
print(c1.nome)
c1.lista_enderecos()
c2 = Cliente("Maria", 20)
c2.insere_endereco("campinas", "SP")
print(c2.nome)
c2.lista_enderecos()
