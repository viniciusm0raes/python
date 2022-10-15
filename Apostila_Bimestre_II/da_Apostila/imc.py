import math
alt = eval(input("informe sua altura em m.cm: "))
p = eval(input("informe seu peso em kg: "))
imc = p/math.pow(alt,2)

if (imc <= 18.5):
   print("Seu peso está abaixo do normal.")
elif (18.5 <= imc <= 25):
   print("Seu peso está normal.")
elif (25 < imc < 30):
   print("Seu peso está acima do normal.")
elif (imc >= 30):
   print("Seu peso é excessivo.")