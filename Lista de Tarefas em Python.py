
tarefas = []

def mostrar_tarefas():
    print("\n===== MINHAS TAREFAS =====")

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

def adicionar_tarefa():
    tarefa = input("Digite sua tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def remover_tarefa():
    mostrar_tarefas()

    try:
        numero = int(input("Número da tarefa para remover: "))
        tarefas.pop(numero - 1)
        print("Tarefa removida!")
    except (ValueError, IndexError):
        print("Número inválido!")

while True:
    print("\n===== MENU =====")
    print("1 - Mostrar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_tarefas()
    elif opcao == "2":
        adicionar_tarefa()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        print("Até mais!")
        break
    else:
        print("Opção inválida!")
