# 03 - Faça um programa que verifique e mostre os números entre 1.000 e 2.000 (inclusive) que, quando divididos por 11 produzem resto igual a 2.

for numero in range(1000,2001):
  if numero % 11 == 2:
    print(numero)
