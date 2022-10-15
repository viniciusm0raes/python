media = soma = quant = maior = menor = 0
for quant in range(1, 11):
    num = int(input("Digite um número inteiro: "))
    soma += num
            
    if quant == 1:
       maior = menor = num       
    
    else:
        if num < 0:
            quant -= 1
            soma += 0                    
            num = int(input("O número deve ser inteiro e POSITIVO: "))

        if num > maior:
            maior = num

        if num < menor:
            menor = num       
        
media = (soma / quant)

print("*"*53)
print("\nVocê digitou {} números válidos e a MÉDIA foi {}.".format(quant, media))
print("{} foi o MAIOR valor e {} o MENOR.\n".format(maior, menor))
print("*"*53)
