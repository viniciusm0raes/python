n1 = eval(input('informe um número: '))
n2 = eval(input('informe outro número: '))
op = input("Informe qual operação desejada:\n M (para média)\n Q (para quociente inteiro da divisão do primeiro pelo segundo número)\n R (para o resto da divisão do primeiro pelo segundo): ")

m = (n1 + n2) / 2
q = n1//n2
r = n1%n2

print("\n***************************\n")

if (op == 'm'):
   print("A média entre", n1, "e", n2, "é igual a", m)

elif (op == 'q'):
   print("O quociente da divisão de", n1, "por", n2, "é igual a", q)

elif (op == 'r'):
   print("O resto da divisão de", n1, "por", n2, "é igual a", r)

else:
   print("Operação inválida")