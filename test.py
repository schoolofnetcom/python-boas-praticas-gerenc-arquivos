import getpass

print('=' * 25)
print('Caixa eletronico Hélio')
print('=' * 25)

account_typed = input('Digite sua conta: ')
password_typed = getpass.getpass('Digite sua senha: ')

account_list = {
    '001': {
        'password': '123',
        'name': 'User1',
    },
    '002': {
        'password': '123',
        'name': 'User2',
    }
}

if account_typed in account_list and password_typed == account_list[account_typed]['password']:
    print('A conta {} é valida'.format(account_typed))
else:
    print('A conta {} não existe ou dados inválidos'.format(account_typed))