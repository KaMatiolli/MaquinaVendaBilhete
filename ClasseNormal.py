from Bilhete import Bilhete

class ClasseNormal(Bilhete):
    def __init__(self):
        self.valor = 100

    def imprime(self):
        print(f"O bilhete normal custa: {self.valor}")