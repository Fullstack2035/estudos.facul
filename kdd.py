import time

# Funções de ordenação adaptadas
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j].lower() > lista[j + 1].lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[min_idx].lower() > lista[j].lower():
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# 1. Criar variável do tipo lista
palavras_base = list()

# 2. Ler o arquivo linha a linha com a instrução 'with'
with open("loremipsum.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        # 3. Separar linha em palavras e 4. Atribuir à lista
        palavras_base.extend(linha.split())

print(f"Total de palavras a ordenar: {len(palavras_base)}\n")

# --- Comparação de Performance ---

# Teste Bubble Sort
lista_bubble = palavras_base.copy()
inicio = time.time()
bubble_sort(lista_bubble)
fim = time.time()
print(f"Bubble Sort:    {fim - inicio:.6f} segundos")

# Teste Selection Sort
lista_selection = palavras_base.copy()
inicio = time.time()
selection_sort(lista_selection)
fim = time.time()
print(f"Selection Sort: {fim - inicio:.6f} segundos")

# Teste Método Nativo .sort() (Timsort)
lista_native = palavras_base.copy()
inicio = time.time()
lista_native.sort(key=str.lower)
fim = time.time()
print(f"Método .sort(): {fim - inicio:.6f} segundos")

# --- Escolha do método e gravação do resultado ---
# Como o .sort() nativo é drasticamente mais rápido, utilizaremos o resultado dele.

with open("palavras_ordenadas.txt", "w", encoding="utf-8") as f_saida:
    for p in lista_native:
        f_saida.write(p + "\n")

print("\nArquivo 'palavras_ordenadas.txt' gerado com sucesso!")

