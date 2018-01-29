from main_test import test
print('file',__name__)
# from test.folder import test_file
#
# print(main.accounts_list)
# main.clear()
# print("qualquer coisa")
# print(test_file.variavel)
import os

from bank_account_variables import money_slips, accounts_list

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
print(BASE_PATH)


# file = open(BASE_PATH + '/_file_test.dat', 'w')  # write
# file.write('school of net1111\n')
# file.write('\n')
# file.write('luiz carlos')
# file.close()

# file = open(BASE_PATH + '/_file_test.dat', 'a')  # write
# file.write('school of net1111\n')
# file.write('\n')
# file.write('luiz carlos')
# file.writelines(('sssssssssss', 'aaaaaaaaaaaaa', 'bbbbbbbbbb'))
# file.writelines(['yyyyyyyyyy', '\n', 'eeeeeeeeeee', '\n', 'cccccccccc'])
# file.close()

# file = open(BASE_PATH + '/_file_test.dat', 'r')  # read
# print(file.read())
# print(file.read(10))
# print(file.read(10))
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline(7))
# print(file.readline(7))
# print(file.readline(7))
# print(file.readline(7))
# print(file.readline(7))
# lines = file.readlines()
# line = file.readline()
# while line:
#     print(line)
#     line = file.readline()
# file.close()

# for line in lines:
#    print(line)

def open_file_bank(mode):
    return open(BASE_PATH + '/_bank_file.dat', mode)


# 20=5;50=5;100=5;
def write_money_slips(file):
    for money_bill, value in money_slips.items():
        file.write(money_bill + '=' + str(value) + ';')


def write_bank_accounts(file):
    for account, account_data in accounts_list.items():
        file.writelines((
            account, ';',
            account_data['name'], ';',
            account_data['password'], ';',
            str(account_data['value']), ';',
            str(account_data['admin']), ';'
                                        '\n'
        ))


def read_money_slips(file):
    line = file.readline()
    while line.find(';') != -1:
        semicolon_pos = line.find(';')
        money_bill_value = line[0:semicolon_pos]
        set_money_bill_value(money_bill_value)
        # 20=5000;50=5000
        if semicolon_pos + 1 == len(line):
            break
        else:
            line = line[semicolon_pos + 1:len(line)]


def set_money_bill_value(money_bill_value):
    equal_pos = money_bill_value.find('=')  # 20=5000
    money_bill = money_bill_value[0:equal_pos]
    count_money_bill_value = len(money_bill_value)
    value = money_bill_value[equal_pos + 1:count_money_bill_value]
    print(money_bill, value)
    money_slips[money_bill] = int(value)


def read_bank_accounts(file):
    lines = file.readlines()
    lines = lines[1:len(lines)]
    for account_line in lines:
        extract_bank_account(account_line)


def extract_bank_account(account_line):
    account_data = []
    while account_line.find(';') != -1:
        semicolon_pos = account_line.find(';')
        data = account_line[0:semicolon_pos]
        account_data.append(data)
        if semicolon_pos + 1 == len(account_line):
            break
        else:
            account_line = account_line[semicolon_pos + 1:len(account_line)]
    add_bank_account(account_data)


def add_bank_account(account_data):
    accounts_list[account_data[0]] = {
        'name': account_data[1],
        'password': account_data[2],
        'value': float(account_data[3]),
        'admin': True if account_data[4] == 'True' else 'False',
    }


def load_bank_data():
    file = open_file_bank('r')
    read_money_slips(file)
    file.close()

    file = open_file_bank('r')
    read_bank_accounts(file)
    file.close()


def save_money_slips():
    file = open_file_bank('r')
    lines = file.readlines()
    file.close()
    file = open_file_bank('w')
    lines[0] = ""
    for money_bill, value in money_slips.items():
        lines[0] += money_bill + '=' + str(value) + ';'
    lines[0] += '\n'
    file.writelines(lines)
    file.close()


def delete_file():
    file = open(BASE_PATH + '/_file_to_delete.dat', 'w')
    file.close()
    os.unlink(BASE_PATH + '/_file_to_delete.dat')
