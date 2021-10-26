sal = eval(input("Informe seu salário atual: "))
sto = input("Informe seu setor: ")

a = sal+(sal*0.1)
b = sal+(sal*0.15)
c = sal+(sal*0.2)

print("\n***************************\n")

if (sto == 'a') or (sto == 'A'):
   print("Seu novo salário será de: R$ {:.2f}".format(a).replace(".",",").replace("_","."))

elif (sto == 'b') or (sto == 'B'):
   print("Seu novo salário será de: R$ {:.2f}".format(b).replace(".",",").replace("_","."))

elif (sto == 'c') or (sto == 'C'):
   print("Seu novo salário será de: R$ {:.2f}".format(c).replace(".",",").replace("_","."))

else:
   print("Salário ou setor inválidos")