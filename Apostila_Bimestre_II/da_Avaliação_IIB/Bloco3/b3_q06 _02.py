quant = soma = media = maior = menor = 0

while quant < 10:
    num = int(input("Digite um número inteiro: "))
    soma += num
    quant += 1
    
    if quant == 1:
       maior = menor = num
    
    elif num < 0:
         num = int(input("O número deve ser inteiro e POSITIVO: "))
         soma = (num*0)
         quant = (num*0)

    elif num > maior:
        maior = num

    elif num < menor:
        menor = num 

media = (soma / quant)

print("*"*53)
print("\nVocê digitou {} números válidos e a MÉDIA foi {}.".format(quant, media))
print("{} foi o MAIOR valor e {} o MENOR.\n".format(maior, menor))
print("*"*53)