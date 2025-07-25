#cálculo de IMC

nome = input('Qual é o seu nome? ')
altura = float(input('Qual é sua altura em metros? '))
peso = int(input('Qual é o seu peso em kg? '))


imc = peso / (altura ** 2)
print(f'{nome} tem {altura}m, pesa {peso}kg e seu IMC é {imc}')
