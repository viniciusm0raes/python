mult = int(input("Informe um múltiplo: "))
inic = int(input("Informe o início do intervalo: "))
fim = int(input("Informe o FIM do intervalo: "))
x = inic
while x < fim:
    x += 1
    if x % mult == 0:        
        print ("{} ".format(x), end='')
if mult > fim:
    print ('Nenhum')