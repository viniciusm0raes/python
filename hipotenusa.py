import math

cata = eval(input("informe o cateto adjacente: "))

cato = eval(input("informe o cateto oposto: "))

hipotenusa = math.sqrt(math.pow(cata,2) + math.pow(cato,2))

print("A hipotenusa do triângulo é igual a: ", round(hipotenusa, 2))