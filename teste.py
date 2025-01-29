# din1=int(input('Informe o valor do seu salário por hora: '))
# hr1=int(input("Informe quantas horas você trabalha no mês: "))
# bruto=din1*hr1
# print(f'O valor bruto do seu salário mensal é de: R${bruto},00')
# inss=bruto*0.08
# sind=bruto*0.05
# rend=bruto*0.11
# desc=inss+sind+rend
# liq=bruto-desc
# print(f'O valor destinado ao INSS é de: R${inss}')
# print(f'O valor destinado ao sindicato é de: R${sind}')
# print(f'O valor destinado ao Imposto de Renda é de: R${rend}')
# print(f'O valor líquido do seu salário é de: R${liq}')
# print(f'O valor total dos descontos é de: R${desc}')
# cobertura_por_litro = 3  # metros quadrados por litro
# litros_por_lata = 18      # litros por lata
# preco_por_lata = 80.00    # preço por lata em reais

# # Função para calcular a quantidade de latas e o preço total
# def calcular_tinta(area):
#     # Calculando a quantidade de litros necessários
#     litros_necessarios = area / cobertura_por_litro
#     # Calculando a quantidade de latas necessárias (arredondando para cima)
#     latas_necessarias = -(-litros_necessarios // litros_por_lata)  # arredondamento para cima
#     # Calculando o preço total
#     preco_total = latas_necessarias * preco_por_lata
    
#     return latas_necessarias, preco_total

# # Entrada do usuário
# area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# # Calculo
# latas, preco = calcular_tinta(area)

# # Saída dos resultados
# print(f"\nPara pintar uma área de {area} m², você precisará de {latas} lata(s) de tinta.")
# print(f"O preço total será R$ {preco:.2f}.")

