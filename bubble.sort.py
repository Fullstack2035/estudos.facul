# a. Método bubbleSort que recebe o array como parâmetro
def bubbleSort(array):
    # b. Primeiro laço for para percorrer os elementos do array
    for i in range(len(array)):
        
        # c. Segundo laço for para iterar e comparar os elementos adjacentes
        # O limite 'len(array) - i - 1' evita comparar elementos já ordenados no final
        for j in range(0, len(array) - i - 1):
            
            # d. Condição if para comparar elementos adjacentes
            if array[j] > array[j + 1]:
                # Criar variável auxiliar para a troca (swap)
                temp = array[j]
                
                # Substituir o valor de array[j] pelo próximo
                array[j] = array[j + 1]
                
                # Substituir o valor de array[j+1] pelo valor da variável auxiliar
                array[j + 1] = temp

# e. Fora do método, declara um array de números com 15 posições
# Valores aleatórios para testar a ordenação
meu_array = [54, 26, 93, 17, 77, 31, 44, 55, 20, 1, 88, 12, 10, 6, 42]


bubbleSort(meu_array)

# g. Imprimir o array na tela
print("Array ordenado de forma crescente:")
print(meu_array)