class Pessoa:
    # método construtor
    def __init__(self, nome, idade, cidade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.peso = peso
        self.altura = altura

    def fazer_aniversario(self):
        self.idade += 1

    def comer(self, quantidade):
        self.peso += quantidade

    def emagrecer(self, quantidade):
        self.peso -= quantidade

    def trocar_nome(self, novo_nome):
        self.nome = novo_nome


p1 = Pessoa('Endrio', 21, 'Blumenau', 60, 1.75)
p2 = Pessoa('Andrei', 37, 'Blumenau', 138, 1.99)
p3 = Pessoa('Edna', 36, 'São Paulo', 70, 1.75)

print(p3.idade)
p3.fazer_aniversario()
print(p3.idade)

print(p3.peso)
p3.comer(0.7)
print(p3.peso)

p3.emagrecer(1)
print(p3.peso)
