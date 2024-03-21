# 12 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

primeiro = int(input("Digite o 1º número "))
segundo = int(input("Digite o 2º número "))

for numero in range(primeiro+1,segundo):
  print(numero)
for numero in range(segundo+1, primeiro):
  print(numero)