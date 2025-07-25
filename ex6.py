#Programa que faz contagem de números pares

inicial = int(input('Qual valor deseja iniciar a contagem? '))
final = int(input('Qual valor deseja encerrar a contagem? '))

x = inicial

while (x <= final):
    #verifica se o número é par
    if (x % 2 == 0):
       print(x)
    x = x + 1
