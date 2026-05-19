class Pessoa:
    def __init__(self, falando=False, comendo=False):
        self.falando = falando
        self.comendo = comendo
    def interromper_falar(self):
        if self.falando == False:
            print("A pessoa já está sem falar.")
        else:
            self.falando = False
    def interromper_comer(self):
        if self.comendo == False:
            print("A pessoa já está sem comer.")
        else:
            self.comendo = False
    def comer(self):
        if self.falando == True:
            print("Erro: não é possível comer falando!")
        else:
            self.comendo = True
            print("A pessoa começou a comer.")
    def falar(self, assunto):
        if self.comendo == True:
            print("Erro: não é possível falar comendo!")
        else:
            self.falando = True
            print(f'A pessoa está falando sobre {assunto}.')

p1 = Pessoa()
p1.falar("oi")
p1.interromper_falar()
p1.comer()
p1.interromper_falar()
    