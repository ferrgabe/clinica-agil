from mvcpacientes.controllers.paciente_controller import PacienteController


def menu_pacientes():
    controller = PacienteController()

    while True:
        print("\n=== Menu Pacientes (MVC Pacientes) ===")
        print("1 - Cadastrar paciente")
        print("2 - Listar pacientes (escolher ordenação)")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            _view_cadastrar_paciente(controller)
        elif opcao == "2":
            _view_listar_pacientes_com_strategy(controller)
        elif opcao == "3":
            print("Saindo do módulo de pacientes...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def _view_cadastrar_paciente(controller: PacienteController):
    print("\n=== Cadastro de Paciente ===")
    login = input("Login: ")
    senha = int(input("Senha (apenas números): "))
    nome = input("Nome completo: ")
    email = input("Email: ")
    telefone = int(input("Telefone (apenas números): "))
    cpf = input("CPF (somente números): ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")

    sucesso, mensagem = controller.cadastrar_paciente(
        login=login,
        senha=senha,
        nome=nome,
        email=email,
        telefone=telefone,
        cpf=cpf,
        data_nascimento=data_nascimento,
    )
    print(mensagem)


def _view_ler_opcao_ordenacao() -> str:
    print("\nComo deseja ordenar os pacientes?")
    print("a - Por nome")
    print("b - Por data de cadastro")
    opcao = input("Escolha uma opção (a/b): ").strip().lower()
    return opcao


def _view_listar_pacientes_com_strategy(controller: PacienteController):
    print("\n=== Listagem de Pacientes ===")

    # Se não tem ninguém cadastrado, já avisa
    pacientes_existentes = controller.listar_pacientes()
    if not pacientes_existentes:
        print("Nenhum paciente cadastrado.")
        return

    opcao = _view_ler_opcao_ordenacao()

    if opcao == "a":
        controller.definir_estrategia_listagem_por_nome()
    elif opcao == "b":
        controller.definir_estrategia_listagem_por_data_cadastro()
    else:
        print("Opção de ordenação inválida. Voltando ao menu.")
        return

    pacientes_ordenados = controller.listar_pacientes_ordenados()

    for p in pacientes_ordenados:
        print(
            f"ID: {p.idusuario}, Login: {p.login}, Nome: {p.nome_completo}, "
            f"Email: {p.email}, Telefone: {p.telefone}, "
            f"Data Cadastro: {p.data_cadastro}, CPF: {p.cpf}, "
            f"Data Nascimento: {p.data_nascimento}"
        )
