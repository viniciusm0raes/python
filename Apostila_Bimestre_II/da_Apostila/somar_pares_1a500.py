soma = 0
cont = 0
lst = []
for n in range(1, 500):
    if n%2==0:
        soma += n
        cont += 1

print("\n**************************************\n")
print("O total de números PARES entre 1 e 500 é: {:_.0f} e a soma destes é igual a: {:_.0f}".format(cont, soma).replace("_","."))
print("\n**************************************\n")