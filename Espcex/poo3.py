class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    def inserir_clientes(self,id,nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id:nome}
        else:
            self.__dados['clientes'].update({id:nome})
    @property
    def dados(self):
        return self.__dados
    def lista_clientes(self):
        for id,nome in self.__dados['clientes'].items():
            print(id,nome)
    def apaga_clientes(self,id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_clientes(1,'Joao')
bd.inserir_clientes(2,'Maria')
bd.dados = 'teste'
print(bd.dados)
