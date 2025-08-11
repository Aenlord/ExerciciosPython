nome = 'Vitor'
sobrenome = 'Miguel'
nome_completo = nome + ' ' + sobrenome
valor_total = 0

#PREÇOS
valor_BAP = int(16)
valor_BAM = int(18)
valor_BAG = int(22)
valor_FFP = int(15)
valor_FFM = int(17)
valor_FFG = int(21)

#MENSAGEM DE BOAS VINDAS
print(f'Bem vindo ao restaurante Jabuticaba! Aqui você encontra as melhores marmitas da região! Meu nome é {nome_completo} e será um prazer te atender!')

#CATÁLOGO
while True:
    print('Temos opções de BIFE ACEBOLADO (BA) e de FILÉ DE FRANGO (FF)!')
    print('MENU DE MARMITAS:')
    print('BIFE ACEBOLADO TAMANHO P: R$16,00')
    print('BIFE ACEBOLADO TAMANHO M: R$18,00')
    print('BIFE ACEBOLADO TAMANHO G: R$22,00')
    print('FILÉ DE FRANGO TAMANHO P: R$15,00')
    print('FILÉ DE FRANGO TAMANHO M: R$17,00')
    print('FILÉ DE FRANGO TAMANHO G: R$21,00')

#TIPO DE MARMITA
    sabor = input('Qual o tipo de marmita você deseja? (BA/FF) ')

    while sabor != 'BA' and sabor !='FF':
        print('Sabor inválido. Tente novamente')
        sabor = input('Qual o tipo de marmita você deseja? (BA/FF) ')

    if sabor == 'BA':
        print('BIFE ACEBOLADO')
    
    elif sabor == 'FF':
        print('FILÉ DE FRANGO')

#TAMANHO DA MARMITA
    tamanho = input('Qual o tamanho da sua marmita? (P/M/G) ')

    while tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Tamanho inválido. Tente novamente')
        tamanho = input('Qual o tamanho da sua marmita? (P/M/G) ')
    
    if tamanho == 'P':
        print('Tamanho P')
    elif tamanho == 'M':
        print('Tamanho M')
    elif tamanho == 'G':
        print('Tamanho G')

#MENSAGEM DO PEDIDO
    if sabor == 'BA':
        if tamanho == 'P':
            print('Você escolheu BIFE ACEBOLADO de tamanho P.')
            valor_total = valor_total + valor_BAP
        elif tamanho == 'M':
            print('Você escolheu BIFE ACEBOLADO de tamanho M.')
            valor_total = valor_total + valor_BAM
        else:
            print('Você escolheu BIFE ACEBOLADO de tamanho G.')
            valor_total = valor_total + valor_BAG

    elif sabor == 'FF':
        if tamanho == 'P':
            print('Você escolheu FILÉ DE FRANGO de tamanho P')
            valor_total = valor_total + valor_FFP
        elif tamanho == 'M':
            print('Você escolheu FILÉ DE FRANGO de tamanho M ')
            valor_total = valor_total + valor_FFM
        else:
            print('Você escolheu FILÉ DE FRANGO de tamanho G ')
            valor_total = valor_total + valor_FFG

#DESEJA MAIS ALGUMA COISA?
    resposta = input('Deseja pedir mais alguma coisa? (S/N) ')
    while resposta != 'S' and resposta!= 'N':
        print('Resposta inválida.')
        resposta = input('Deseja pedir mais alguma coisa? (S/N) ')
    if resposta == 'N':
        print('Obrigado pela preferência! Volte sempre ao Jabuticaba!')
        print(f'Valor total: R${valor_total}')
        break
        

