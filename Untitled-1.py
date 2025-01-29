#1
print('Hello, World!')

#2
num=int(input('Digite um número: '))
print(f'O número informado foi: {num}')

#3
num1=int(input('Digite outro número: '))
soma=num+num1
print(f'A soma dos números é: {soma}')

#4
n1=float(input('Nota 1: '))
n2=float(input('Nota 2: '))
n3=float(input('Nota 3: '))
n4=float(input('Nota 4: '))
media=(n1+n2+n3+n4)/4
print(f'A média do aluno foi: {media}')
if media>=6:
    print("O aluno foi aprovado")
else:
    print('O aluno foi reprovado')

#5
med=float(input("Insira uma medida em metros: "))
cen=med*100
print(f'Esta medida equivale a: {cen}cm')

#6
raio=float(input("Insira o valor do raio de uma circunferência em cm: "))
area=raio**2*3.14
print(f'A área deste círculo seria de aproximadamente: {area}cm²')

#7
lado=float(input('Insira o valor de um dos lados de um quadrado em cm: '))
area1=lado**2*2
print(f'O dobro da área deste quadrado é de: {area1}cm²')

#8
din=int(input('Informe o valor do seu salário por hora: '))
hr=int(input("Informe quantas horas você trabalha no mês: "))
mes=din*hr
print(f'O valor do seu salário mensal é de: R${mes},00')

#9
F=int(input('Insira uma temperatura em °F: '))
C=5*((F-32)/9)
print(f'Esta temperatura corresponde a {C}°C')

#10
C1=int(input('Insira uma temperatura em °C'))
F1=1.8*C1+32
print(f'Esta temperatura corresponde a {F1}°F')

#11
i1=int(input('Digite um número inteiro: '))
i2=int(input('Digite outro número inteiro: '))
r1=float(input('Digite um número real:'))
a=2*i1*i2/2
b=3*i1+r1
c=r1**3
print(f'o produto do dobro do primeiro com metade do segundo é: {a}')
print(f'a soma do triplo do primeiro com o terceiro é: {b}')
print(f'o terceiro elevado ao cubo é: {c}')

#12
altura=float(input("digite sua altura: "))
p=(72.7*altura)-58
print(f'O seu peso ideal é de: {p}kg')

#13
sexo=input("informe seu sexo (utilize f para feminino e m para masculino): ")
h=float(input('digite a sua altura em metros: '))
if sexo=='f':
    f=(62.1*h)-44.7
    print(f'seu peso ideal é de: {f}kg')
elif sexo=='m':
    m=(72.7*h)-58
    print(f'seu peso ideal é de: {m}kg')
else: print('sexo inválido')

#14
peso=float(input('informe o peso do peixe em kg: '))
if peso>50:
    excesso=(peso-50)
    multa=excesso*4
    print(f'Peixe tem {excesso}kg de excesso, resultando em R${multa} de multa')
else: print('Peixe não tem excesso de peso.')

#15
din1=int(input('Informe o valor do seu salário por hora: '))
hr1=int(input("Informe quantas horas você trabalha no mês: "))
bruto=din1*hr1
print(f'O valor bruto do seu salário mensal é de: R${bruto},00')
inss=bruto*0.08
sind=bruto*0.05
rend=bruto*0.11
desc=inss+sind+rend
liq=bruto-desc
print(f'O valor destinado ao INSS é de: R${inss}')
print(f'O valor destinado ao sindicato é de: R${sind}')
print(f'O valor destinado ao Imposto de Renda é de: R${rend}')
print(f'O valor líquido do seu salário é de: R${liq}')
print(f'O valor total dos descontos é de: R${desc}')

#16
area2=float(input('informe o tamanho da área que será pintada, em m²: '))
lata=area2/3//18
if lata%True:
    print(f'você precisa de {lata+1} lata(s)')
else:
    print(f'você precisa de {lata} lata(s)')
    
# Estrutura De Decisão
#1
nm=int(input('digite um número: '))
nm1=int(input('digite outro número: '))
if nm>nm1:
    print(f'o maior número é: {nm}')
elif nm==nm1:
    print('os números são iguais')
else:
    print(f'o maior número é: {nm1}')

#2
sex=input('informe seu sexo')