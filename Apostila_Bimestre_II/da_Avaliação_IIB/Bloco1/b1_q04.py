import math
a = eval(input("informe um ângulo: "))

a = a
S = math.sin(math.radians(a))
C = math.cos(math.radians(a))
T = math.tan(math.radians(a))

print("\n***************************\n")

print("O seno de {} é {:.2f} \nO cosseno de {} é {:.2f} \nA tangente de {} é {:.2f}".format(a,S,a,C,a,T))
print("\n***************************\n")