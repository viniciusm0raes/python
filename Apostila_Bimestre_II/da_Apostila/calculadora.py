print("Bem vindo à Calculadora.")
num1 = eval(input("Informe um número: "))
num2 = eval(input("Informe outro número: "))
op = input("Informe a operação:\n + para Adição\n - para Subtração\n * para multiplicação\n / para divisão: ")

if op == '+':
    print("A soma de ", num1, "e", num2, " é: ", num1 + num2)
elif op == '-':
    print(num2, "subtraído de", num1, "resulta em: ", num1 - num2)
elif op == '*':
    print(num1, "multiplicado por", num2, "é igual a:", num1 * num2)
elif op == '/':
    print(num1, "dividido por", num2, "é igual a:", num1 / num2)
else:
    print("Operação inválida")