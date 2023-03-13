from file import *
from interface import *
from time import sleep

arq_name = 'tarefas.txt'
options = ['Ver Tarefas', 'Criar Tarefa', 'Remover Tarefa', 'Sair do Programa']

if not fileExists(arq_name):
    createFile(arq_name)

while True:
    option = menu(options, min=1, max=len(options))
    if option == 1:
        readFile(arq_name)
        sleep(2)

    elif option == 2:
        tarefa = input('Descreva a tarefa: ')
        sleep(1)
        addTask(arq_name, tarefa)

    elif option == 3:
        readFile(arq_name)
        sleep(2)
        index = int(input('Digite o indíce da tarefa que deseja remover: '))
        deleteTask(arq_name, index)
    
    elif option == 4:
        print('-' * 50)
        print('\nSaindo do sistema... Muito obrigado!')
        print('-' * 50)
        break