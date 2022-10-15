graos = 1
total = 0
for casa in range (1, 65):
  total = total + graos
  print(casa, ": {:_.0f}".format(graos).replace(".",",").replace("_","."))
  graos = graos * 2
print("Total: {:_.0f}".format(total).replace(".",",").replace("_","."))