n1 = eval
n2 = eval

while True:
    n1 = eval(input("Digite um número para soma: "))
    if (n1==0):
        print("Fim do programa.")
        break
    n2 = eval(input("Digite outro número para soma: "))

    if (n2==0):
        print("Fim do programa.")
        break

    soma = (n1+n2)
    print("A soma dos dois valores é:",soma)