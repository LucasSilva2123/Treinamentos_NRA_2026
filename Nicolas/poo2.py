class Produto:
    def __init__(self, nome : str, preco : float):
        self.nome = nome;
        self.preco = preco;

    def desconto(self, percentual):
        self._preco -= self.preco * self.desconto / 100.0
    
    def print_informacoes(self):
        print(f"Nome = {self.nome}")
        print(f"Preço = {self.preco}");

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace("R$", ""));
        
        self._preco = valor;
    
    @property
    def nome(self):
        return self._nome;

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str):
            valor = valor.upper();
        
        self._nome = valor;

p1 = Produto("Mandioca", "R$5.0");
p1.print_informacoes()