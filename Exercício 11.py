# 11 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

# impares
for contador in range(1,51):
  if contador % 2 == 1:
    print(contador, end= " ")
print()

# Pares
for numero in range(1,51):
  if numero % 2!= 1:
    print(numero, end= " ")
