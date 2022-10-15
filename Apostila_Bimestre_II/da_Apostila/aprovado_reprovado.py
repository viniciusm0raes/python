n1 = eval(input("Infomre a PRIMEIRA nota: "))
n2 = eval(input("Informe a SEGUNDA nota: "))
opt = eval(input("Informe o valor da Nota Optativa: "))

if (opt != -1) and (n1 > n2) and (opt > n2):
    media = (n1 + opt) / 2
elif (opt != -1) and (n2 > n1) and (opt > n1):
    media = (n2 + opt) / 2
else:
    media = (n1 + n2) / 2

if (media >= 6):
     print("Aprovado com média: ", media)
elif  (media < 3):
     print("Reprovado com média: ", media)
else:
     print("Vc foi pra recuperação com média: ", media)