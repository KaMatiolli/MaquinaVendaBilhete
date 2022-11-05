from Bilhete import Bilhete

class PrimeiraClasse(Bilhete):
    def __init__(self):
        self.valor = self.valor * 2

    def __repr__(self):
       print("Esse é o bilhete de primeira classe com acrescimo: {self.valor = self.valor * 2}")
