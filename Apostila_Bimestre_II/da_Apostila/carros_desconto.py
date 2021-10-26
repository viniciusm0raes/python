qa2000 = qd2000 = tcarros = desc1 = desc2 = vtab = 0
resp = 'S' or 'N'
while resp == 'S':
    ano = int(input("Informe o ano do veículo: "))
    vtab = eval(input("Informe o valor de tabela do veículo: R$ "))

    if ano <= 2000:
        vtab == vtab
        qa2000 += 1
        desc1 = vtab - (vtab * 0.12)
        print("\nO valor do veículo(s) é R$ {:_.2f} e com o desconto será de: R$ {:_.2f}".format(
            vtab, desc1).replace(".",",").replace("_","."))
        print("\n", "* "*13)

    elif ano > 2000:
        vtab == vtab
        qd2000 += 1
        desc2 = vtab - (vtab * 0.07)
        print("\nO valor do veículo(s) é R$ {:_.2f} e com o desconto será de: R$ {:_.2f}".format(vtab, desc2).replace(".",",").replace("_","."))
        print("\n", "* "*13)

    tcarros=qa2000 + qd2000

    resp=str(input("Quer consultar outro veículo? [S/N] ")).upper().strip()[0]

if resp == 'N':
    print("\n", "* "*13)
    print("Você pesquisou {} veículo(s) com ano até 2000 em um total de {} veículo(s).".format(
        qa2000, tcarros))
    print("\n", "* "*13)