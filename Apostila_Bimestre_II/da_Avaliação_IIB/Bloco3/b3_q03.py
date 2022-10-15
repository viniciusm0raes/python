num = int(input("Listar os números ímpares menores que: "))

lst = []
for n in range(num-1):
    if n%2==1:
        lst.append(n)

print("\n**************************************\n")
print("","Os números ímpares menores que ", num, "são:",lst)
print("\n**************************************\n")