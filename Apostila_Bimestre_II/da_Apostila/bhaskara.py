import math
a = eval(input("informe o valor de a: "))
b = eval(input("informe o valor de b: "))
c = eval(input("informe o valor de c: "))

d = math.pow(b,2) - (4 * a * c)

print("\n********************************************\n")

if (d == 0):
  print("Apenas uma raiz real (delta = 0)")

elif (d < 0):
  print("Não há raízes reais, pois o delta é menor que zero.")

elif (a == 0):
  print("Não é uma equação do segundo grau, pois o a é igual a zero.")

else:
  r1 = (-b + math.sqrt(d)) / (2 * a)
  r2 = (-b - math.sqrt(d)) / (2 * a)
  print("X' é igual a: ", r1, "\nX'' é igual a: ", r2)
print("\n********************************************\n")