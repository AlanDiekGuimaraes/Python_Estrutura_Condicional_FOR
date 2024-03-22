# 05 - Faça um programa que leia 5 números e informe o maior número.

maior_numero = float('-inf')
for contador in range(1,6):
  numero = float(input(f"Informe o {contador}º número: "))
  if numero > maior_numero:
    maior_numero = numero
  print(f"O maior número digitado foi: {maior_numero}")
