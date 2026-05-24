class BaseDeDados:
    def __init__(self):
        self.dados : dict = {}
    
    def inserir_clientes(self, id, nome):
        if not "clientes" in self.dados:
            self.dados["clientes"] = {id : nome}
        else:
            self.dados["clientes"].update({id : nome})
    
    def lista_clientes(self):
        for id, nome in self.dados["clientes"].items():
            print(f"{id} : {nome}");
    
    def apaga_clientes(self, id):
        del self.dados["clientes"][id]

base_de_dados : BaseDeDados = BaseDeDados();

base_de_dados.inserir_clientes(0, "Maria");
base_de_dados.inserir_clientes(0, "Maria A.");
base_de_dados.inserir_clientes(1, "Ricardo");
base_de_dados.inserir_clientes(2, "Oswald");

base_de_dados.lista_clientes() # Funciona

base_de_dados.dados = "Uma string qualquer"

# base_de_dados.lista_clientes() # Não funciona

class BaseDeDados:
    def __init__(self):
        self.__dados : dict = {}
    
    def inserir_clientes(self, id, nome):
        if not "clientes" in self.dados:
            self.dados["clientes"] = {id : nome}
        else:
            self.dados["clientes"].update({id : nome})
    
    def lista_clientes(self):
        for id, nome in self.dados["clientes"].items():
            print(f"{id} : {nome}");
    
    def apaga_clientes(self, id):
        del self.dados["clientes"][id]
    
    @property
    def dados(self):
        return self.__dados

base_de_dados : BaseDeDados = BaseDeDados();

base_de_dados.inserir_clientes(0, "Maria");
base_de_dados.inserir_clientes(0, "Maria A.");
base_de_dados.inserir_clientes(1, "Ricardo");
base_de_dados.inserir_clientes(2, "Oswald");

base_de_dados.lista_clientes()

# base_de_dados.dados = "Uma string qualquer" # Não funciona
base_de_dados.__dados = "Uma string qualquer"

base_de_dados.lista_clientes() # Funciona