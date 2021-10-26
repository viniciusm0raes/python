x = somid = somalt = idade = idam = altura = altm = medalt = medida = 0
idam = 0
altm = 0
for x in range(1, 6):
    idade = int(input("Informe a idade do aluno {}: ".format(x)))
    altura = float(input("Informe a altura do aluno (m.cm) {}: ".format(x)))
           
    if altura < 1.7:        
        somid += idade
        idam += 1
        medida = somid/idam

    elif idade > 20:
        somalt += altura
        altm += 1
        medalt = somalt/altm

print("-"*30)
print("Os alunos com menos de 1,70m de altura têm uma média de idade igual a: {:.2f} ou {:.0f} arredondando.".format(medida, medida))
print("\nJá os alunos com mais de 20 anos de idade, têm uma altura média de igual a: {:.2f} ".format(medalt))
print("-"*30)