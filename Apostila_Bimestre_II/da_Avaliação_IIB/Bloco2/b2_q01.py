calc = 'S' or 'N'
while True:    
    calc = str(input("Deseja calcular a potência de algum número? \n S para Sim \n N para Não\n")).upper().strip()[0]
    print("-" * 13)
    if (calc == 'S'):
        ba = eval(input("Digite o valor da base: "))
        ex = eval(input("Digite o valor do expoente: "))
        res = ba**ex

        print("-" * 13)
        print("O resultado é = {:_.0f}".format(res).replace(".",",").replace("_","."))
        print("-" * 13)

    if (calc == 'N'):
        print("cabô...rUmbora...")
        break