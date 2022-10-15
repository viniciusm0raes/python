quant = soma = media = maior = menor = 0

while quant < 10:
    num = int(input("Digite um número inteiro: "))
    soma += num
    quant += 1
    if quant == 1:
       maior = menor = num
    
    elif num < 0:
        num = 0
        num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num 
media = (soma / quant)
print("Você digitou {} números e a MÉDIA foi {}.".format(quant, media))
print("O MAIOR valor foi {} e o MENOR foi {}.".format(maior, menor))

