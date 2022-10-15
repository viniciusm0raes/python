import math

raio = eval(input('informe o raio do círculo: '))

diam = 2*raio

area = math.pi*math.pow(raio,2)

perim = (2*(math.pi)*raio)

print('O diâmetro do cículo é: ', round(diam, 2))
print('A área do cículo é: ', round(area, 2))
print('O perímetro do cículo é: ', round(perim, 2))