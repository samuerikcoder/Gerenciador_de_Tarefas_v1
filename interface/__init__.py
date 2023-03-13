def header(txt):
    '''
    Exibe uma frase ou palavra entre duas linhas pontilhadas com 50 caracteres '-'.

    :param txt: frase ou palavra que será exibida.
    :type txt: str
    :return: None

    '''
    print('-' * 50)
    print(txt.center(50))
    print('-' * 50)

    
def menu(options, min, max):
    '''
    Cria uma interface com o usuário para que ele possa visualizar determinadas opções.

    :param options: Lista com opções para o usuário interagir.
    :type options: list
    :param min: número correspondente a primeira opção.
    :type min: int
    :param max: número de opções máximas que o usuário poderá escolher.
    :type max: int
    :return: o número da opção que o usuário escolheu.
    rtype: int

    '''
    header('Gerenciador de tarefas')

    for number, option in enumerate(options):
        print(f'{number + 1} - {option}')

    while True:
        resposta = int(input(f'\nDigite um número de {min} até {max}: '))

        if resposta in range(min, max+1):
            break
            
        print(f'{resposta} não é válido, digite novamente')
        

    print('-' * 50)

    return resposta

