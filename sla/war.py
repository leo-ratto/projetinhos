
import random

while True:

    dados_ataque = []
    dados_defesa = []

    a = 0
    b = 0

    print()

    ataque = int(input('Dados de ataque: '))
    for i in range(ataque):
        dados_ataque.append(random.randint(1, 6))
        print(f'Dado {i+1}: {dados_ataque[i]}')

    print()

    defesa = int(input('Dados de defesa: '))
    for n in range(defesa):
        dados_defesa.append(random.randint(1, 6))
        print(f'Dado {n+1}: {dados_defesa[n]}')

    print()
    
    if ataque < defesa:
        for x in range(ataque):
            if max(dados_defesa) >= max(dados_ataque):
                a += 1
            else:
                b += 1
            dados_ataque.remove(max(dados_ataque))
            dados_defesa.remove(max(dados_defesa))
    
    else:
        for n in range(defesa):
            if max(dados_defesa) >= max(dados_ataque):
                a += 1
            else:
                b += 1
            dados_ataque.remove(max(dados_ataque))
            dados_defesa.remove(max(dados_defesa))

    if b == 1:
        print(f'Ataque ganhou em {b} dado')
    elif b > 1:
        print(f'Ataque ganhou em {b} dados')
        
    if a == 1:
        print(f'Defesa ganhou em {a} dado')
    elif a > 1:
        print(f'Defesa ganhou em {a} dados')

    print()

    sla = input()
    if sla != '':
        break
