import json

# Função para carregar dados de um arquivo JSON
def carregar_dados(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Função para salvar dados em um arquivo JSON
def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f)

# Função para incluir dados genéricos
def incluir_dados(arquivo, dado, codigo_key='codigo'):
    dados = carregar_dados(arquivo)

    # Verifica se o código já existe
    for item in dados:
        if item[codigo_key] == dado[codigo_key]:
            print(f"Código {dado[codigo_key]} já existe.")
            return

    dados.append(dado)
    salvar_dados(arquivo, dados)
    print(f'{dado} incluído com sucesso!')

# Função para listar dados genéricos
def listar_dados(arquivo, tipo):
    dados = carregar_dados(arquivo)
    if not dados:
        print(f'Nenhum {tipo} cadastrado.')
    else:
        for i, dado in enumerate(dados, start=1):
            print(f"{i}. {dado}")

# Função para excluir dados genéricos
def excluir_dados(arquivo, tipo):
    dados = carregar_dados(arquivo)
    listar_dados(arquivo, tipo)
    if dados:
        indice = int(input(f"Digite o número do {tipo} que deseja excluir: ")) - 1
        if 0 <= indice < len(dados):
            excluido = dados.pop(indice)
            salvar_dados(arquivo, dados)
            print(f'{excluido} excluído com sucesso!')
        else:
            print(f'Número inválido.')

# Função para alterar dados genéricos
def alterar_dados(arquivo, tipo, codigo_key='codigo'):
    dados = carregar_dados(arquivo)
    listar_dados(arquivo, tipo)
    if dados:
        indice = int(input(f"Digite o número do {tipo} que deseja alterar: ")) - 1
        if 0 <= indice < len(dados):
            novo_dado = input(f"Digite o novo dado para o {tipo}: ")
            dados[indice] = novo_dado
            salvar_dados(arquivo, dados)
            print(f'{tipo} alterado com sucesso!')
        else:
            print('Número inválido.')

# Funções específicas para cada entidade
def menu_estudante():
    while True:
        print("\n--- Menu Estudante ---")
        print("1. Incluir estudante")
        print("2. Listar estudantes")
        print("3. Excluir estudante")
        print("4. Alterar estudante")
        print("5. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Digite o nome do estudante: ")
            idade = int(input("Digite a idade do estudante: "))
            matricula = input("Digite a matrícula do estudante: ")
            estudante = {"codigo": matricula, "nome": nome, "idade": idade}
            incluir_dados('estudantes.json', estudante)
        elif opcao == '2':
            listar_dados('estudantes.json', 'estudante')
        elif opcao == '3':
            excluir_dados('estudantes.json', 'estudante')
        elif opcao == '4':
            alterar_dados('estudantes.json', 'estudante')
        elif opcao == '5':
            break
        else:
            print("Opção inválida!")

def menu_disciplina():
    while True:
        print("\n--- Menu Disciplina ---")
        print("1. Incluir disciplina")
        print("2. Listar disciplinas")
        print("3. Excluir disciplina")
        print("4. Alterar disciplina")
        print("5. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            codigo = int(input("Digite o código da disciplina: "))
            nome = input("Digite o nome da disciplina: ")
            disciplina = {"codigo": codigo, "nome": nome}
            incluir_dados('disciplinas.json', disciplina)
        elif opcao == '2':
            listar_dados('disciplinas.json', 'disciplina')
        elif opcao == '3':
            excluir_dados('disciplinas.json', 'disciplina')
        elif opcao == '4':
            alterar_dados('disciplinas.json', 'disciplina')
        elif opcao == '5':
            break
        else:
            print("Opção inválida!")

def menu_professor():
    while True:
        print("\n--- Menu Professor ---")
        print("1. Incluir professor")
        print("2. Listar professores")
        print("3. Excluir professor")
        print("4. Alterar professor")
        print("5. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            codigo = int(input("Digite o código do professor: "))
            nome = input("Digite o nome do professor: ")
            cpf = input("Digite o CPF do professor: ")
            professor = {"codigo": codigo, "nome": nome, "cpf": cpf}
            incluir_dados('professores.json', professor)
        elif opcao == '2':
            listar_dados('professores.json', 'professor')
        elif opcao == '3':
            excluir_dados('professores.json', 'professor')
        elif opcao == '4':
            alterar_dados('professores.json', 'professor')
        elif opcao == '5':
            break
        else:
            print("Opção inválida!")

def menu_turma():
    while True:
        print("\n--- Menu Turma ---")
        print("1. Incluir turma")
        print("2. Listar turmas")
        print("3. Excluir turma")
        print("4. Alterar turma")
        print("5. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            codigo = int(input("Digite o código da turma: "))
            codigo_professor = int(input("Digite o código do professor: "))
            codigo_disciplina = int(input("Digite o código da disciplina: "))
            turma = {"codigo": codigo, "codigo_professor": codigo_professor, "codigo_disciplina": codigo_disciplina}
            incluir_dados('turmas.json', turma)
        elif opcao == '2':
            listar_dados('turmas.json', 'turma')
        elif opcao == '3':
            excluir_dados('turmas.json', 'turma')
        elif opcao == '4':
            alterar_dados('turmas.json', 'turma')
        elif opcao == '5':
            break
        else:
            print("Opção inválida!")

def menu_matricula():
    while True:
        print("\n--- Menu Matrícula ---")
        print("1. Incluir matrícula")
        print("2. Listar matrículas")
        print("3. Excluir matrícula")
        print("4. Alterar matrícula")
        print("5. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            codigo_turma = int(input("Digite o código da turma: "))
            codigo_estudante = int(input("Digite o código do estudante: "))
            matricula = {"codigo_turma": codigo_turma, "codigo_estudante": codigo_estudante}
            incluir_dados('matriculas.json', matricula, codigo_key='codigo_turma')
        elif opcao == '2':
            listar_dados('matriculas.json', 'matrícula')
        elif opcao == '3':
            excluir_dados('matriculas.json', 'matrícula')
        elif opcao == '4':
            alterar_dados('matriculas.json', 'matrícula')
        elif opcao == '5':
            break
        else:
            print("Opção inválida!")

# Menu principal
def menu_principal():
    while True:
        print("\n--- Sistema de Gerenciamento Acadêmico ---")
        print("1. Gerenciar estudantes")
        print("2. Gerenciar disciplinas")
        print("3. Gerenciar professores")
        print("4. Gerenciar turmas")
        print("5. Gerenciar matrículas")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            menu_estudante()
        elif opcao == '2':
            menu_disciplina()
        elif opcao == '3':
            menu_professor()
        elif opcao == '4':
            menu_turma()
        elif opcao == '5':
            menu_matricula()
        elif opcao == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

# Executa o menu principal
menu_principal()
