import math
a = eval(input('informe um ângulo: '))

S = math.sin(math.radians(a))
C = math.cos(math.radians(a))
T = math.tan(math.radians(a))

print("\n***************************\n")

print("O seno de", a, "é", round(S,3), "\nO cosseno de", a, "é igual a", round(C,3), "\nA tangente de", a, "é igual a", round(T,3))