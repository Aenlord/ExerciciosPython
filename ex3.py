#O programa apresenta um menu com três frutas: maçã, laranja e banana. O usuário escolhe uma fruta (1, 2 ou 3) e informa a quantidade desejada.
# O programa calcula e exibe o valor total da compra com base nos preços: maçã (R$2,30), laranja (R$3,60) e banana (R$1,85). 
# Caso a opção seja inválida, uma mensagem de erro é mostrada.

print('Escolha o que deseja comprar: ')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual sua escolha? '))
qtd = int(input('Quantas unidades? '))
if (produto == 1):
    pagar = qtd * 2.3
    print(f'Você comprou {qtd} maçãs. Total à pagar: {pagar}')
elif (produto == 2):
    pagar = qtd * 3.6
    print(f'Você comprou {qtd} laranjas. Total à pagar: {pagar}')
elif (produto == 3):
    pagar = qtd * 1.85
    print(f'Você comprou {qtd} bananas. Total à pagar: {pagar}')
else:
    print('Produto inexistente!')
