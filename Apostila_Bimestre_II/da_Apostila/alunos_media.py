alunos = 1
while (alunos <= 5):
     n1 = eval(input("Informe a primeira nota: "))
     n2 = eval(input("Informe a segunda nota: "))
     media = (n1 + n2)/2     
     
     if (media >= 6):
          print("Média do aluno", alunos, " é ", media, "e a situação é aprovado.")
          
     elif (media < 4):
          print("Média do aluno", alunos, " é ", media, "e a situação é reprovado.")
     else:
          print("Média do aluno", alunos, " é ", media, "e a situação é em recuperação.")

     alunos += 1