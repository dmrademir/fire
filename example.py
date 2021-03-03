import fire

x = 'Teste'


def ola(nome='Ademir'):
    """ Função para dizer olá"""
    return f"Olá {nome}!"


def f_text(txt='amostra'):
    print(f'*' * 50)
    print(f'-' * 50)
    print(f"{txt:^50}")
    print(f'-' * 50)
    print(f'*' * 50)


fire.Fire()
