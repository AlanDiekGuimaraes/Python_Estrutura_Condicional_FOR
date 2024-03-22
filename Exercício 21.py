# 21 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

impares = 0
pares = 0

for contador in range(1,11):
  numero =  int(input(f"Digite o {contador}º número INTEIRO: "))
  if numero % 2 == 1:
    impares += 1
  else:
    pares += 1
print(f'''
Números pares: {pares}
Números impares: {impares}''')