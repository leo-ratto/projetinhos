
user = 'Usuario Sem Criatividade'
senha = 'SenhaSegura123'

for i in range(3):
    login_u = input('Insira seu nome de usuário: ')
    login_s = input('Insira sua senha: ')
    
    if login_s == senha and login_u == user:
        print('\fAcesso concedido. Bem vindo')
        break
    
    else:
        print('\fNome de usuário ou senha inválidos. Tente novamente')
        
if i == 2:
    print('\fNúmero máximo de tentativas excedido. Acesso Bloquedo')
    
