# 02 - Faça um programa que leia 5 números e informe o maior número.

maior_numero = float('-inf')

for contador in range(5):
  numero = float(input(f"Digite o {contador+1}º número "))
  if  numero > maior_numero:
    maior_numero = numero

  print(f"O maior numero digitado é: {maior_numero}")