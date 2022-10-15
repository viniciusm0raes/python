for x in range(10, 0, -1):
    c = x
    f = 1

    if x%2==1:

        print('Calculando {:_.0f}! = '.format(x), end=''.replace(".",",").replace("_","."))
        while c > 0:
            print('{:_.0f}'.format(c), end=''.replace(".",",").replace("_","."))
            print(' x ' if c > 1 else ' =', end=''.replace(".",",").replace("_","."))
            f *= c
            c -= 1
        print (' {:_.0f} '.format(f).replace(".",",").replace("_","."))
print ('Tico sofreu muito, mas saiu...')