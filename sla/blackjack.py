
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
            print()
            bet = float(input('Adicione sua aposta: '))
            print()
            
        if bet < 5:
            print('Aposta inválida. A aposta deve ser maior que 5 créditos')
            print()
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
    
    vm_dealer.append(valor_cartas[nm_dealer[0]])
    
    n = 0
    
    while True:
        
        if 0 in nmr_mao and soma_mao <= 11:

            if n == 0 and 10 in valor_mao:
                show_mao = '21'
            else:
                show_mao = f'{soma_mao}/{soma_mao + 10}'
                
            if soma_mao == 11:
                break

        else:
            show_mao = str(soma_mao)

        show_cartas = 'Jogador: '
        
        for i in range(len(mao)):
            show_cartas += str(mao[i])
            show_cartas += ' '
            
        show_cartas += f'| {show_mao}'
        
        if nm_dealer[0] == 0:
            show_dealer = f'Dealer: {dealear[0]} 🂠 | 1/10'
            print(show_dealer)
        
        else:
            show_dealer = f'Dealer: {dealear[0]} 🂠 | {valor_cartas[vm_dealer[0]-1]}'
            print(show_dealer)
            
        print(show_cartas)
        
        if n == 1 and acao == 'd':
            break
        
        if soma_mao >= 21:
            break            
            
        if 0 in nmr_mao and soma_mao == 11 and n == 0:
            soma_mao = 21
            break

        elif n == 0 and bet * 2 <= credito:
            print('Double (d) | Hit (h) | Stand (s)')

        else:
            print('Hit (h) | Stand (s)')
        
        print()
            
        acao = input('Ação: ')

        if acao == 'h':

            nmr_mao.append(random.randint(0,12))
            nmr_naipe.append(random.randint(0,3))

            mao.append(cartas[nmr_mao[i+1]] + naipe[nmr_naipe[i+1]])

            valor_mao.append(valor_cartas[nmr_mao[i+1]])

            soma_mao = sum(valor_mao)
            
            n += 1

        elif acao == 's':
            break
        
        elif n == 0 and bet * 2 < credito and acao == 'd':
        
            bet *= 2
            
            nmr_mao.append(random.randint(0,12))
            nmr_naipe.append(random.randint(0,3))
            
            mao.append(cartas[nmr_mao[i+1]] + naipe[nmr_naipe[i+1]])
            
            valor_mao.append(valor_cartas[nmr_mao[i+1]])
            
            soma_mao = sum(valor_mao)
            n += 1
            
        else:
            print()
            print('Ação inválida')
  
        print()
        
    soma_dealer = vm_dealer[0]
    
    print()
    
    r = 0
    while soma_dealer < 17:
        
        if soma_mao > 21:
            break
        
        nm_dealer.append(random.randint(0,12))
        nn_dealer.append(random.randint(0,3))    
            
        dealear.append(cartas[nm_dealer[r+1]] + naipe[nn_dealer[r+1]])
        
        vm_dealer.append(valor_cartas[nm_dealer[r+1]])
        
        soma_dealer += vm_dealer[r+1]

        p_dealer = 'Dealer: '

        for i in range(len(dealear)):
            p_dealer += str(dealear[i])
            p_dealer += ' '

        if 0 in nm_dealer:
            
            if 10 in vm_dealer:
                
                if r == 0:
                    soma_dealer += 10
                    p_dealer += '| 21'
                    break

        if soma_dealer <= 11 and 0 in nm_dealer:
            sv_dealer = f'| {soma_dealer}/{soma_dealer + 10}'
            p_dealer += sv_dealer
                        
            if soma_dealer + 10 >= 17:
                soma_dealer += 10
                break
                   
        else:
            p_dealer += f'| {soma_dealer}'

        r += 1
    
    if soma_mao > 21:
        print(show_dealer)
    else:
        print(p_dealer)
    print(show_cartas)
        
    print()
    
    if 0 in nmr_mao:
        if soma_mao <= 11:
            soma_mao += 10
            
        if n == 0:
            if 10 in valor_mao:
                if soma_mao == 21:
                    if soma_mao > soma_dealer:
                        print('BLACKJACK!')
                        retorno = 1.5 * bet
    
    if soma_mao > 21:
        print('Busted!')
        retorno = (-bet)
                
    elif soma_mao == soma_dealer:
        retorno = 0
        print('Push')
        
    elif soma_mao < soma_dealer:
        if soma_dealer > 21:
            retorno = bet
            print('Player win!')
        
        else:
            retorno = (-bet)
            print ('Dealer win!')
            
    elif soma_mao > soma_dealer:
        retorno = bet
        print('Player win!')
        
    credito += retorno
    
    print()
    
    continuar = input('Pressione Enter para continuar: ')
    if continuar != '':
        break
    else:
        print()