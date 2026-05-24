class Pessoa:
    comendo : bool = False;
    falando : bool = False;

    def __init__(self, nome : str, idade : int):
        self.nome = nome;
        self.idade = idade;
    
    def comer(self, alimento : str):
        if self.comendo:
            print(f"{self.nome} já está comendo")
            return;
        
        if self.falando:
            print(f"{self.nome} não pode comer enquanto está falando")
            return;

        self.comendo = True;
        print(f"{self.nome} está comendo {alimento}")

    def interromper_comer(self):
        if self.comendo:
            self.comendo = False
            print(f"{self.nome} não está mais comendo");
    
    def falar(self, assunto : str):
        if self.falando:
            print(f"{self.nome} já está falando")
            return;
        
        if self.comendo:
            print(f"{self.nome} não pode falar enquanto está comendo")
            return;

        self.falando = True;
        print(f"{self.nome} está falando sobre {assunto}")

    def interromper_falar(self):
        if self.falando:
            self.falando = False
            print(f"{self.nome} não está mais falando");

p1 : Pessoa = Pessoa("Pedro", 25);
p1.comer("mandioca");
p1.falar("o fim do mundo")
p1.interromper_comer();
p1.falar("o fim do mundo");


