p = eval(input("informe uma opção de Prato Principal:\n 1 - Vegetariano (R$ 10,00)\n 2 - Peixe (R$ 20,00)\n 3 - Frango (R$ 10,00)\n 4 - Carne (R$ 15,00)\n 0 - Nenhuma\n "))
s = eval(input("informe uma opção de Sobremesa:\n 1 - Pudim (R$ 3,00)\n 2 - Sorvete (R$ 7,50)\n 3 - Mousse (R$ 4,00)\n 4 - Gelatina (R$ 1,50)\n 0 - Nenhuma\n "))
b = eval(input("informe uma opção de Bebida:\n 1 - Chá (R$ 2,00)\n 2 - Suco de Fruta (R$ 5,00)\n 3 - Suco de Polpa (R$ 3,50)\n 4 - Refrigerante (R$ 6,00)\n 0 - Nenhuma\n "))

print("\n***************************\n")

if (p == 1):
   cp = 10

elif (p == 2):
  cp = 20

elif (p == 3):
  cp = 10

elif (p == 4):
  cp = 15

else:
  cp = 0

if (s == 1):
  cs = 3

elif (s == 2):
  cs = 7.5

elif (s == 3):
  cs = 4

elif (s == 4):
  cs = 1.5

else:
  cs = 0

if (b == 1):
  cb = 2

elif (b == 2):
  cb = 5

elif (b == 3):
  cb = 3.5

elif (b == 4):
  cb = 6

else:
  cb = 0

ct = (cp + cs + cb)

print("O valor da sua conta é: R$ {:.2f}".format(ct).replace(".",",").replace("_","."))
