x = eval(input("Informe um número "))

t1 = x%3
t2 = x%5

if (t1)==0 and (t2)==0:
  print(x, "é um número divisível por 3 e 5.")

else:
  print(x, "não é um número divisível por 3 e 5.")