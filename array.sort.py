import random

# 1. Criar array de 15 posições com números inteiros aleatórios
numeros = [random.randint(1, 100) for _ in range(15)]
print(f"Original (Inteiros): {numeros}")

# 2. Ordenação crescente com .sort()
numeros.sort()
print(f"Crescente:           {numeros}")

# 3. Ordenação decrescente com key=None e reverse=True
numeros.sort(key=None, reverse=True)
print(f"Decrescente:         {numeros}")