while True:
    num = int(input("\nDeseja conhecer o fatorial de qual número? "))
    c = num
    f = 1
    if num < 0:
        print("Valor negativo, programa ecerrado.")
        break

    print('Calculando {:_.0f}! = '.format(num), end=''.replace(".",",").replace("_","."))
    while c > 0:
        print('{:_.0f}'.format(c), end=''.replace(".",",").replace("_","."))
        print(' x ' if c > 1 else ' =', end=''.replace(".",",").replace("_","."))
        f *= c
        c -= 1
    print (' {:_.0f} '.format(f).replace(".",",").replace("_","."))