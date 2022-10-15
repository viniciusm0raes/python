while True:
    tab = eval(input("Vc deseja consultar a tabuada de qual número? "))
    print("-" * 13)
    if tab < 0:
        print("Vc digitou um número negativo")
        break
    
    for n in range(1, 11):
        print(f"{tab} x {n} = {tab * n:.2f}".format(tab, n))

    print("-" * 13)
print("Fim do programa Tabuada.")