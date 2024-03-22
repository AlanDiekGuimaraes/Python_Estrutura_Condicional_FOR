# 17 - Uma loja tem tem uma política de descontos de acordo com o valor da compra do cliente. Os descontos começam acima dos R$500.

# A cada 100 reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até 25%.

# Por exemplo: R$500 = 1% || R$600,00 = 2% ... etc...

# Faça um programa que exiba essa tabela de descontos no seguinte formato: Valordacompra – porcentagem de desconto – valor final



valor = float(input('Digite o valor da compra: R$'))
contagem = 1
if valor >= 600 and contagem:
    reduzido = valor - 500
    if reduzido >= 100 or contagem <= 24:
        for x in range(999):
            contagem += 1
            reduzido -= 100
            if reduzido < 100 or contagem == 24:
                break
porcentagem = contagem / 100
desconto = valor * porcentagem
final = valor - desconto
print(f'O produto de R${valor:.2f} ficará a partir de R${final:.2f} com {contagem:.0f}% de desconto.')
