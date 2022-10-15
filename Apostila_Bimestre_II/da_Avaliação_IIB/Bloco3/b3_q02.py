ii = int(input("Informe o início de um intervalo: "))
fi = int(input("Informe o final desse mesmo intervalo: "))
inc = int(input("Determine o incremento: "))
for x in range(ii, fi, inc):
    print("{} ".format(x), end="")
