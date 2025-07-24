A = float(input('Digite o primeiro lado do triângulo: '))
B = float(input('Digite o segundo lado do triângulo: '))
C = float(input('Digite o terceiro lado do triângulo: '))

if((A > 0 and B > 0 and C > 0) and (A + B > C and B + C > A and A + C > B)):
    #Se chegou até aqui o triângulo é válido
    if (A != B and A != C and B != C):
        print('Triângulo escaleno')
    elif A==B and B == C:
            print('Triângulo equilátero')
    else:
            print('Triângulo isósceles! ')


else:
    (print ('Ao menos um dos valores indicados não servem para formar um triângulo.'))

    
