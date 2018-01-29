# import bank_account_variables
from bank_account_variables import accounts_list, money_slips
import getpass

from file import save_money_slips


def do_operation(option_typed, account_auth):
    if option_typed == '1':
        show_balance(account_auth)
    elif option_typed == '10' and accounts_list[account_auth]['admin']:
        insert_money_slips()
    elif option_typed == '2':
        withdraw()


def show_balance(account_auth):
    print('Seu saldo é %s' % accounts_list[account_auth]['value'])


def insert_money_slips():
    amount_typed = input('Digite a quantidade de cédulas: ')
    money_bill_typed = input('Digite a cédula a ser incluída: ')
    # money_slips[money_bill_typed] = money_slips[money_bill_typed] + int(amount_typed)
    money_slips[money_bill_typed] += int(amount_typed)
    print(money_slips)


def withdraw():
    value_typed = input('Digite o valor a ser sacado: ')

    money_slips_user = {}
    value_int = int(value_typed)

    if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
        money_slips_user['100'] = value_int // 100
        value_int = value_int - value_int // 100 * 100

    if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
        money_slips_user['50'] = value_int // 50
        value_int = value_int - value_int // 50 * 50

    if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
        money_slips_user['20'] = value_int // 20
        value_int = value_int - value_int // 20 * 20

    if value_int != 0:
        print('O caixa não tem cédulas disponíveis para este valor')
    else:
        for money_bill in money_slips_user:
            money_slips[money_bill] -= money_slips_user[money_bill]
        save_money_slips()
        print('Pegue as notas:')
        print(money_slips_user)


def auth_account():
    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')

    if account_typed in accounts_list and password_typed == \
            accounts_list[account_typed]['password']:
        return account_typed
    else:
        return False


def get_menu_options_typed(account_auth):
    print("1 - Saldo")
    print("2 - Saque")
    if accounts_list[account_auth]['admin']:
        print("10 - Incluir cédulas")
    return input('Escolha uma das opções acima: ')
