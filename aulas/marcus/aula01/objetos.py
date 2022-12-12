
class Pessoa():
    #metodo de instancia usa o self
    def __init__(self,nome,marca,idade=0):#Metodo de iniciar
        self.nome = nome
        self.idade =idade
        self.falando = False
        self.celular = Celular(marca)

    def falar(self,assunto):
        if self.falando:
            print(f'{self.nome} nao pode falar sobre {assunto} pois ja esta falando sobre outro assunto')
        else:
            print(f'{self.nome} esta falando sobre {assunto}')
            self.falando = True

    def parar_de_falar(self):
        self.falando = False
        print(f'{self.nome} parou de falar')
    
    

class Celular():
    def __init__(self,modelo):
        self.modelo=modelo

    def conectar(self):
        print(f'O {self.modelo} conectou a rede')