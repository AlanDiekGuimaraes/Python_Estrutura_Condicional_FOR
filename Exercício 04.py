# 04- Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.

numero = int(input("Digite um número para ver sua tabuada: "))

print(f"Tabuada de {numero}:")
for contador in range(1, 11):
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")