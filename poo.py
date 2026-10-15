class dog():
    def __init__(self, raça, nome, idade):
        self.raça = raça
        self.nome = nome
        self.idade = idade

    def latir(self):
        print(f"{self.nome} latiu")
dog1 = dog("golden", "pimba", 8)
dog2 = dog("boxer", "zeus", 9)
dog3 = dog("pug", "costelinha", 4)

print (f"nome do dog3 : {dog3.nome}")

dog2.latir()
dog1.latir()
dog3.latir()