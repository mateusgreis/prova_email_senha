import email.contentmanager

email_cadastrado = 'correto@correto.com'
senha_cadastrada = 'senhacorreta123'

while True:
    email = input('Digite o e-mail: ')
    senha = input('Digite a senha: ')
    if email != email_cadastrado or senha != senha_cadastrada:
        print('E-mail ou senha incorretos! Tente novamente.')
    else:
        print('Acesso permitido!')
        break
