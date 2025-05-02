
import random

cartas = ['A']

for i in range(9):
    cartas.append(f'{i+2}')
    
cartas.append('J')
cartas.append('Q')
cartas.append('K')

valor_cartas = []

for i in range(10):
    valor_cartas.append(i+1)
    
for i in range(3):
    valor_cartas.append(10)

naipe = ['♠', '♣', '♥', '♦']

credito = 100

while True:
    print(f'Saldo atual: {credito}')
    
    print()
    
    if credito < 5:
        print('Saldo insuficiente. Fim de jogo')
        break

    bet = float(input('Adicione sua aposta: '))
    
    print()
    
    while bet > credito or bet < 5:
        
        if bet > credito:
            print(f'Aposta inválida. A aposta excede o saldo atual ({credito})')
            bet = float(input('Adicione sua aposta: '))
            print()
            
        if bet < 5:
            print('Aposta inválida. A aposta deve ser maior que 5 créditos')
            bet = float(input('Adicione sua aposta: '))
            print()
        
    mao = []
    nmr_mao = []
    nmr_naipe = []
    valor_mao = []
        
    for i in range(2):
        nmr_mao.append(random.randint(0,12))
        nmr_naipe.append(random.randint(0,3))
        
        add = cartas[nmr_mao[i]] + naipe[nmr_naipe[i]]
        
        mao.append(add)
        
        valor_mao.append(valor_cartas[nmr_mao[i]])
        
    soma_mao = sum(valor_mao)
    
    dealear = []
    nm_dealer = []
    nn_dealer = []
    vm_dealer = []

    nm_dealer.append(random.randint(0,12))
    nn_dealer.append(random.randint(0,3))    
        
    dealear.append(cartas[nm_dealer[0]] + naipe[nn_dealer[0]])
    
    n = 0
    
    while True:
        
        if 0 in nmr_mao and soma_mao < 10:
            show_mao = f'{soma_mao}/{soma_mao + 10}'
        else:
            show_mao = str(soma_mao)
        
        show_cartas = 'Jogador: '
        
        for i in range(len(mao)):
            show_cartas += str(mao[i])
            show_cartas += ' '
            
        show_cartas += f'| {show_mao}'
            
        print(f'Dealer: {dealear[0]}  🂠')
        print(show_cartas)
        
        if soma_mao >= 21:
            break            
        
        if n == 0 and bet * 2 < credito:
            print('Hit (h) | Double (d) | Stand (s)')
        else:
            print('Hit (h) | Stand (s)')
            
        print()
        acao = 'r' #input('Ação: ')
        
        if acao == 'h':
            
            nmr_mao.append(random.randint(0,12))
            nmr_naipe.append(random.randint(0,3))
            
            mao.append(cartas[nmr_mao[i]] + naipe[nmr_naipe[i]])
            
            valor_mao.append(valor_cartas[nmr_mao[i]])
            
            soma_mao = sum(valor_mao)
            
        elif acao == 's':
            break
        
        elif n == 0 and bet * 2 < credito and bet == 'd':
        
            bet *= 2
            
            nmr_mao.append(random.randint(0,12))
            nmr_naipe.append(random.randint(0,3))
            
            mao.append(cartas[nmr_mao[i]] + naipe[nmr_naipe[i]])
            
            valor_mao.append(valor_cartas[nmr_mao[i]])
            
            soma_mao = sum(valor_mao)        
        else:
            print()
            print('Acão inválida')
  
        n += 1
        print()
    
    #se n = 0 e soma é 21, verifica se foi blackjack
    #ver se soma da bust
    
    credito -= bet