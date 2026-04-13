# 1. Abrir um arquivo chamado "texto.txt" para escrita ("w")
# O modo "w" (write) cria o arquivo se ele não existir
arquivo = open("texto.txt", "w", encoding="utf-8")

# 2. Criar uma lista usando a sintaxe solicitada
texto = list()

# 3. Utilizando o método "append", atribuir frases para a lista
texto.append("Esta é a primeira linha do meu arquivo.\n")
texto.append("O Python facilita muito a manipulação de arquivos.\n")
texto.append("Estou aprendendo a escrever dados externamente.\n")

# 4. Escrever o conteúdo da lista no arquivo aberto
# O método writelines() é ideal para escrever listas de strings
arquivo.writelines(texto)

# Fechar o arquivo para garantir que os dados sejam salvos fisicamente no disco
arquivo.close()

print("Arquivo 'texto.txt' criado com sucesso!")