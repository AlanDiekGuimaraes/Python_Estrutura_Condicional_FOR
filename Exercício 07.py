# 07 - Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
for contador in range (1,6):
  numero = float(input(f"Digite o {contador}º números "))
  soma += numero
print(f"A soma dos 5 números é: {soma} e a media é: {soma/contador}")
