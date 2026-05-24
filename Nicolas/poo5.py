class Produto:
    def __init__(self, nome : str, preco : float):
        self.nome = nome;
        self.preco = preco;

class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []
    
    def inserir_produto(self, produto : Produto):
        self.produtos.append(produto);
    
    def inserir_produtos(self, produtos : list[Produto]):
        for produto in produtos:
            self.inserir_produto(produto);

    def listar_produtos(self):
        for produto in self.produtos:
            print(f"{produto.nome} - R${produto.preco :.2f}");
    
    def valor_compra(self) -> float:
        total = 0;
        for produto in self.produtos:
            total += produto.preco;
        return total

    @property
    def produtos(self) -> list[Produto]:
        return self.__produtos;

carrinho_de_compras = CarrinhoDeCompras();

carrinho_de_compras.listar_produtos(); # Nada é printado
print(f"Total no carrinho {carrinho_de_compras.valor_compra() :.2f}") # Total é sempre 0

p1 = Produto("Sabonete", 4.2);
p2 = Produto("Shampoo", 10.5);
p3 = Produto("Geladeira eletrolux 3 portas", 12000.0);

carrinho_de_compras.inserir_produtos([p1, p2, p3]);

carrinho_de_compras.listar_produtos();
print(f"Total no carrinho {carrinho_de_compras.valor_compra() :.2f}")