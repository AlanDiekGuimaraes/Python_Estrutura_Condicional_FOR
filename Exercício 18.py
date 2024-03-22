# 18 -  Faça um programa que receba a idade de 15 pessoas e que calcule e mostre:

# a) A quantidade de pessoas em cada faixa etária;

# b) A percentagem de pessoas na primeira e na última faixa etária, com relação ao total de pessoas:

# Até 15 anos

# De 16 a 30 anos

# De 31 a 45 anos

# De 46 a 60 anos

# Acima de 61 anos

ate15 = 0
de16a30 = 0
de31a45 = 0
de46a60 = 0
maior60 = 0
for contador in range(1,16):
  idade = int(input(f"Digite a {contador}ª idade "))
  if idade <= 15:
    ate15 +=   1
  elif idade >=16 and idade <=30:
    de16a30 += 1
  elif idade >= 31 and idade <=45:
    de31a45 += 1
  elif idade >=46 and idade <= 60:
    de46a60 += 1
  else:
    maior60 += 1
    #arrumar porcentagem
porcentagem15 = (ate15/contador) * 100
porcentagem60 = (maior60/contador) * 100
print(f'''
 {ate15} pessoas entre 0 a 15 anos
 {de16a30} pessoas entre 16 e 30 anos
 {de31a45} pessoas entre 31 e 45 anos
 {de46a60} pessoas entre 46 e 60 anos
 {maior60} pessoas acima de 61 anos
  ''')
print(f'''

A porcetagem de pessoas de 0 a 15 anos é de {porcentagem15:.2f}%
A porcetagem de pessoas de 0 a 60 anos é de {porcentagem60:.2f}%

''')