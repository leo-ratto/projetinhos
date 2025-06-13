'''Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas.

Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0. Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.

Ao final, exiba a média geral da turma.'''

num = int(input('\fInsira o número de alunos para o cálculo da média: '))

soma_geral = 0

for i in range(num):
    aluno = input('\fInsira o nome do aluno: ')
    
    soma_aluno = 0
    
    for n in range(3):
        nota = float(input(f'Insira o valor da nota {n+1}: '))
        
        soma_aluno += nota
        
    media_aluno = soma_aluno / 3
    
    soma_geral += media_aluno
    
    print(f'\fA média do(a) aluno(a) {aluno} foi: {media_aluno:.1f}')
          
    if media_aluno >= 7:
        print(f'O aluno(a) {aluno} foi aprovado')
        
    else:
        print(f'O aluno(a) {aluno} foi reprovado')
        
media_geral = soma_geral / num

print(f'\fA média da turma foi: {media_geral:.1f}')