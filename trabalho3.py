nome_completo = 'Vitor de Souza Miguel'
modelo = 0
quantidade_camisetas = 0
desconto = 0
adicional_frete = 0
valor_camisa = 0

#função para a escolha do modelo
def escolha_modelo():
    while True:
        modelo = input ('Escolha o modelo desejado (MCS/MLS/MCE/MLE): ').strip().upper()
        if modelo in ['MCS','MLS','MCE','MLE']:
            return modelo
        else:
            print('Essa opção não é válida. Tente novamente!')

#função para definir a quantidade de camisetas e a relação com o desconto adquirido
def num_camisetas():
    while True:
        try:
            quantidade_camisetas = int(input('Quantas camisetas? (máximo 20000) '))
            if 0 < quantidade_camisetas <= 20000:
                if quantidade_camisetas < 20:
                   desconto = 0
                elif quantidade_camisetas >=20 and quantidade_camisetas < 200:
                   desconto = 0.05
                elif quantidade_camisetas >=200 and quantidade_camisetas < 2000:
                   desconto = 0.07
                elif quantidade_camisetas >=2000 and quantidade_camisetas < 20000:
                   desconto = 0.12
                return quantidade_camisetas, desconto
            else: print('Valor inválido. Digite um número entre 1 e 20000')
        except ValueError:
            print('Valor inválido. Escolha um número inteiro')

#função para a escolha do frete
def frete():
    while True:
        try:
            tipo_frete = int(input('Qual tipo de frete você deseja?\n1 - Transportadora (R$100)\n2 - Sedex (R$200)\n3 - Retirar o pedido na fábrica (R$0) \n'))
            if tipo_frete == 1:
                adicional_frete = 100
            elif tipo_frete == 2:
                adicional_frete = 200
            elif tipo_frete == 3:
                adicional_frete = 0
                    
            else:
                print('Código inválido. Tente novamente.')
                continue

            return adicional_frete
        except ValueError:
            print('Digite apenas números (1, 2 ou 3).')
                      
#Código principal
print(f'Bem vindo a fábrica de camisetas do {nome_completo}\nTemos as seguintes opções de camisas:\nMCS - Manga Simples\nMLS - Manga Longa Simples\nMCE - Manga Curta com Estampa\nMLE - Manga Longa com Estampa')

modelo = escolha_modelo()
quantidade_camisetas, desconto = num_camisetas()
adicional_frete = frete()

if modelo == 'MCS':
    valor_camisa = 1.8
elif modelo == 'MLS':
    valor_camisa = 2.1
elif modelo == 'MCE':
    valor_camisa = 2.9
elif modelo == 'MLE':
    valor_camisa = 3.2

total_pagar = valor_camisa*quantidade_camisetas + adicional_frete

print(f'Você escolheu {quantidade_camisetas} camisetas do modelo {modelo}\nValor do frete: R${adicional_frete}\nValor total a pagar: R${total_pagar}')
     