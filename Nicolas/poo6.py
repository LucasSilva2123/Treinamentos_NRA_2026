class Endereco:
    def __init__(self, cidade : str, estado : str):
        self.cidade = cidade;
        self.estado = estado;
    
    def print_endereco(self):
        print(f"{self.cidade}, {self.estado}")

    def __del__(self):
        print(f"Endereço ({self.cidade}, {self.estado}) foi deletado")

class Cliente():
    def __init__(self, nome : str, idade : int):
        self.nome = nome;
        self.idade = idade;
        self.__enderecos = [];
    
    def inserir_endereco(self, cidade : str, estado : str):
        self.enderecos.append(Endereco(cidade, estado));

    def lista_enderecos(self):
        for endereco in self.enderecos:
            endereco.print_endereco();
    
    def __del__(self):
        print(f"{self.nome} for apagado");
    
    @property
    def enderecos(self) -> list[Endereco]:
        return self.__enderecos

cliente = Cliente("Josué", 32);
cliente.inserir_endereco("Pintopolis", "São Paulo")
cliente.inserir_endereco("xique-xique", "Bahia")

del cliente;