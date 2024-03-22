# 24 - A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o enésimo termo.

soma = 0
primeiro = 1
segundo = 1
numero =  int(input("Digite um valor para criamos a série de Fibonacci: "))
print("FOR")
print(primeiro, segundo, end=" ")
for contador in range(1, numero + 1):
    soma = primeiro + segundo
    primeiro = segundo
    segundo = soma
    print(soma, end=" ")
#==========================================
print(" ")
print("WHILE")
soma = 0
primeiro = 1
segundo = 1
contador = 0
print(primeiro, segundo, end=" ")
while contador < numero:
    soma = primeiro + segundo
    primeiro = segundo
    segundo = soma
    contador +=1
    print(soma, end=" ")