inic = int(input("Informe o início do intervalo: "))
fim = int(input("Informe o final do intervalo: "))
mult = int(input("Digite o múltiplo que deseja pesquisar: "))
lst = []

for n in range(inic, (fim+1)):
    if (n%mult==0):
        lst.append(n)

print("\n**************************************\n")
print("Os múltiplos de {} entre {} e {} são: \n{}".format(mult, inic, fim, lst))
print("\n**************************************\n")

