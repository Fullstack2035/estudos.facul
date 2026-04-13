# --- Passo 3: Operações com o método open() ---

# Criar uma variável e atribuir o conteúdo do arquivo com o método "open"
arquivo = open("loremipsum.txt", "r", encoding="utf-8")

# Imprimir todo o conteúdo do arquivo
print("--- Conteúdo Total do Arquivo ---")
print(arquivo.read())

# Reposicionar o cursor para o início do arquivo para novas leituras
arquivo.seek(0)

# Imprimir apenas a primeira linha do arquivo
print("\n--- Apenas a Primeira Linha ---")
print(arquivo.readline(), end="")

# Imprimir apenas os 3 primeiros caracteres do arquivo
# (Note: O comando abaixo lê do ponto onde o cursor parou ou do início se resetado)
arquivo.seek(0)
print("\n\n--- 3 Primeiros Caracteres ---")
print(arquivo.read(3))

# Fechar o arquivo aberto manualmente
arquivo.close()


# --- Passo 3: Operação com a instrução "with" ---

print("\n\n--- Leitura utilizando a instrução 'with' ---")
# O 'with' garante que o arquivo seja fechado automaticamente após o uso
with open("loremipsum.txt", "r", encoding="utf-8") as arquivo_with:
    conteudo = arquivo_with.read()
    print(conteudo)