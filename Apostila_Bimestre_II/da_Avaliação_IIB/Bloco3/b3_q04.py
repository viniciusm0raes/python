inic = int(input("Informe o início do intervalo: "))
fim = int(input("Informe o final do intervalo: "))
lst = []
soma = 0
for n in range(inic, fim+1):
    lst.append(n)
    soma += n

print("\n**************************************\n")
print(lst, "=", soma)
print("\n**************************************\n")