import random

def prever_dado(faces):
    acertos = 0
    print(f"\n--- Testando Dado de {faces} faces ---")
    
    for i in range(3):
        numeroprevisto = random.randint(1, faces)
        numerododado = int(input(f"Escolha um número (1 a {faces}): "))
        
        if numerododado == numeroprevisto:
            print("Acertou!")
            acertos += 1
        else:
            print("Não acertou")
        print(f"O número previsto foi: {numeroprevisto}")
    
    print(f"Total de acertos no dado com {faces}: {acertos}")

prever_dado(4)
prever_dado(6)
prever_dado(8)
prever_dado(10)
prever_dado(12)
prever_dado(20)
prever_dado(100)