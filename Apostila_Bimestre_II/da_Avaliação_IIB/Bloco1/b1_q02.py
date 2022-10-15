val = eval(input("Informe o valor na etiqueta do produto: "))
pag = (input("Informe a forma de pagamento:\n d para em dinheiro\n c para à vista no cartão de crédito\n d2 dividido em 2 vezes\n d3 dividido em 3 vezes: "))

d = (val-(val*0.1))
c = val-(val*0.05)
d2 = val/2
d3 = (val+(val*0.1))/3

print("\n***************************\n")

if (pag == 'd'):
   print("O pagamento será à vista no valor de: R$ {:_.2f}".format(d).replace(".",",").replace("_","."))

elif (pag == 'c'):
   print("O valor do pagamento será de: R$ {:_.2f}".format(c).replace(".",",").replace("_","."))

elif (pag == 'd2'):
   print("O valor do pagamento será de 2 parcelas de: R$ {:_.2f}".format(d2).replace(".",",").replace("_","."))

elif (pag == 'd3'):
   print("O valor do pagamento será em 3 parcelas de: R$ {:_.2f}".format(d3).replace(".",",").replace("_","."))

else:
   print("Valor informado inválido")