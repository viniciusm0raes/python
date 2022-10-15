primos=[]
n1 = int(input("Informe um número: "))
n2 = int(input("Informe um número maior que o anterior: "))

for x in range(n1, n2 + 1):
    cont=0
    for y in range(n1, x + 1):
        if x%y==0:
            cont+=1
        
    if cont<=2:
        primos.append(x)
print(primos)