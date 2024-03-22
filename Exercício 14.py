# 14 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

pares = 0
impares = 0

for contador in range (1,11):
  numero = int(input(f"Digite o {contador}º número "))
  if numero % 2 == 1:   #Verifica se o numero dividido por 2 tem o resto igual a 1, se sim ele é impar. para verificar se os numeros eram pares usaria ( if numero % 2 == 0:)
    impares  += 1       # incrementa a contagem dos numeros impares
  else:
    pares += 1
print(f'''Números pares = {pares}
Números impares = {impares}''')
