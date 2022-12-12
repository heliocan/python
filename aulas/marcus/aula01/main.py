from objetos import  Pessoa

p1 = Pessoa('Marcus','samsung',20)
p2 = Pessoa('Joao','iphone',20)


print(p1.nome)
print(p2.nome)
p1.falar('futebol')
p1.falar('games')
p1.parar_de_falar()
p1.falar('carro')

p1.celular.conectar()