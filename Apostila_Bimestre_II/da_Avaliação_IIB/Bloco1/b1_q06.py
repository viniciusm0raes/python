n1 = eval(input('informe um número: '))
n2 = eval(input('informe outro número: '))
op = input("Informe qual operação desejada:\n M (para média)\n Q (para quociente inteiro da divisão do primeiro pelo segundo número)\n R (para o resto da divisão do primeiro pelo segundo): ")

m = (n1 + n2) / 2
q = n1//n2
r = n1%n2

print("\n***************************\n")

if (op == 'm'):
   print("A média entre {:_.0f} e {:_.0f} = {:_.2f}".format(n1, n2, m))

elif (op == 'q'):
   print("O quociente da divisão de {:_.0f} por {:_.0f} = {:_.2f}".format(n1, n2, q))

elif (op == 'r'):
   print("O resto da divisão de {:.0f} por {:.0f} = {:.2f}".format(n1, n2, r))

else:
   print("Operação inválida")
