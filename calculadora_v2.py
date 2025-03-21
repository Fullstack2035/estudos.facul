def calculadora():
    print("calculadora")
    print("Operações disponíveis:")
    print("+ : Adição")
    print("- : Subtração")
    print("* : Multiplicação")
    print("/ : Divisão")

    operacao = input("Escolha uma operação (+, -, *, /): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero!")
            return
    else:
        print("Operação inválida!")
        return

    print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")

calculadora()