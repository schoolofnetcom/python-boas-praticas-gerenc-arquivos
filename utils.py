import os


def clear():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)


def header():
    print("****************************************")
    print("*** School of Net - Caixa Eletrônico ***")
    print("****************************************")
