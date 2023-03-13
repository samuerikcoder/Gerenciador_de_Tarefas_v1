from interface import header

def fileExists(name):
    '''
    Verifica se um arquivo existe no diretório atual.

    :param name: O nome do arquivo que será verificado.
    :type name: str
    :return: Retorna True se o arquivo existir e False se o arquivo não existir.
    :rtype: bool
    :raises: FileNotFoundError: Se o arquivo especificado não for encontrado.
    '''
    try:
        exe = open(name, 'rt')
        exe.close()
    except FileNotFoundError:
        return False
    
    return True

def createFile(name):
    '''
    Cria um arquivo com nome escolhido.

    :param name: O nome que será atribuído ao arquivo.
    :type name: str
    :raises: Exception: Se não for possível criar o arquivo
    :return: None

    '''
    try:
        exe = open(name, 'wt+')
        exe.close()
    except:
        print('Não foi possível criar o arquivo')
    else:
        print(f'O arquivo {name} foi criado com sucesso!')

def readFile(name):
    '''
    Lê um arquivo e exibe a lista de tarefas.

    :param name: O nome do arquivo que será lido.
    :type name: str
    :raise: Exception: Se não for possível ler o arquivo.

    
    '''
    try:
        tarefas = open(name, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        header('Tarefas Para Concluir')
        for number, tarefa in enumerate(tarefas):
            print(f'Tarefa {number + 1} - {tarefa}')
    finally:
        tarefas.close() 

def addTask(arq_name, task='Não há nada por aqui'):
    '''
    Adiciona uma nova tarefa a um arquivo existente.

    :param arq_name: O nome do arquivo em que a tarefa será adicionada.
    :type arq_name: str
    :param task: A descrição da tarefa a ser adicionada ao arquivo. O valor padrão é 'Não há nada por aqui'.
    :type task: str
    :raises: Exception: Se não for possível abrir o arquivo especificado.
    :raises: Exception: Se não for possível escrever no arquivo especificado.
    :return: None
    '''
    try:
        tarefas = open(arq_name, 'at')
    except Exception:
        raise Exception('Não foi possível abrir o arquivo especificado.')
    else:
        try:
            tarefas.write(task + '\n')
        except Exception:
            raise Exception('Houve um erro na hora de escrever o arquivo especificado.')
        else:
            print('Nova tarefa adicionada!')
            tarefas.close()

def deleteTask(arq_name, index):
    '''
    Deleta uma tarefa(linha) do arquivo pelo índice.

    :param arq_name: nome do arquivo em que a tarefa será removida.
    :type arq_name: str
    :param index: índice da tarefa que será deletada.
    :type index: int
    :raises: Exception: Se não for possível abrir o arquivo especificado.
    :raises: Exception: Se o índice da tarefa escolhida não existir
    :return: None

    '''
    try:
        with open(arq_name,'r') as f:
            tarefas = f.readlines()
    except:
        print('Não foi possível abrir o arquivo!')
    else:
        try:
           tarefas.pop(index - 1)
        except:
            print('Essa tarefa não existe, logo não pode ser deletada')
        else:
            with open(arq_name, 'w') as f:
                for tarefa in tarefas:
                    f.write(tarefa)
            print(f'Tarefa-{index} foi removida com sucesso!')