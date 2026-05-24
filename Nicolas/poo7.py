class Pessoa:
    def __init__(self, nome : str, idade : int):
        self.nome = nome;
        self.idade = idade;
        self.nomeclasse = self.__class__.__name__;
    
    def falar(self):
        print(f"{self.nome} está falando");

class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nome} esta estudando");

class Cliente(Pessoa):
    def comprar(self):
        print(f"{self.nome} está comprando");

pessoa = Pessoa("Maria", 21);
aluno = Aluno("Renato", 24);
cliente = Cliente("Paulo", 31);

pessoa.falar();
aluno.falar();
cliente.falar();

# pessoa.estudar(); # Não funciona
aluno.estudar();
# cliente.estudar(); # Não funciona

# pessoa.comprar(); # Não funciona
# aluno.comprar(); # Não funciona
cliente.comprar();