m = eval(input("informe o valor em Metros: "))
cv = input("Informe qual conversão desejada:\n mm (para milímetros)\n cm (para centímetros)\n km (para quilômetros): ")

print("\n***************************\n")

mm = (m * 1000)
cm = (m * 100)
km = (m / 1000)

if (cv == 'mm'):
  print(m,"m", "convertido para milímetros é igual a: ", mm,"mm")

elif (cv == 'cm'):
  print(m,"m", "convertido para centímetro é igual a: ", cm,"cm")

elif (cv == 'km'):
  print(m,"m", "convertido para quilômetros é igual a: ", km,"km")

else:
    print("Conversão inválida")
