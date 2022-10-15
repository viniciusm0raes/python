sexo = (input("Informe seu sexo com m para masculino ou f para feminino\n "))

altura = eval(input("Informe sua altura em metros / centímetros (m.cm): "))

if (sexo == "m"):
  print ("Seu peso ideal é: ", (altura*72.7)-58, "kg")
else:
  print ("Seu peso ideal é: ", (altura*62.1)-44.7, "kg")