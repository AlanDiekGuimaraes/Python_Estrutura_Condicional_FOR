# 22 - Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles.

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

if segundo_numero > primeiro_numero:
    for intervalo in range(primeiro_numero +1, segundo_numero):
        print(intervalo)
else:
    for intervalo in range(segundo_numero +1, primeiro_numero):
        print(intervalo)