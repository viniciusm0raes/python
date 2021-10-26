x = eval(input("Em que ano vc nasceu? "))

idade = 2021-x
falta = idade-18

if (idade)>=18:
  print('Vc tem ', idade, 'anos, fazem ', abs(falta), 'anos que vc já pode tirar a habilitação.')

else:
  print('Vc tem ', idade, 'anos, esperar', abs(falta), 'anos para poder tirar a sua habilitação.')
