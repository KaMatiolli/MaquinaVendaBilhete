from ClasseNormal import ClasseNormal
from PrimeiraClasse import PrimeiraClasse

primeira = PrimeriaClasse()
normal = ClasseNormal()

while True:
    print("\n")
    print("- Bem-vindo! Escolha o bilhete desejado ? -")
    print("- 1. Classe economica (normal)            -")
    print("- 2. Primeira classe                      -")

    entrada = int(input("Entrada.: "))

    if entrada == 1: 
        normal.imprime()
    elif entrada == 2: 
        primeira.imprime()
    elif entrada == 3: 
        break
    else:
        print("Entrada invalida, digite umas das opções a acima, por favor!")