from mvcpacientes.controllers.paciente_controller import PacienteController


def menu_pacientes():
    controller = PacienteController()

    while True:
        print("\n=== Menu Pacientes (MVC Pacientes) ===")
        print("1 - Cadastrar paciente")
        print("2 - Listar pacientes")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            _view_cadastrar_paciente(controller)
        elif opcao == "2":
            _view_listar_pacientes(controller)
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


def _view_listar_pacientes(controller: PacienteController):
    print("\nPacientes cadastrados:")
    pacientes = controller.listar_pacientes()
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    for p in pacientes:
        print(
            f"ID: {p.idusuario}, Login: {p.login}, Nome: {p.nome_completo}, "
            f"Email: {p.email}, Telefone: {p.telefone}, "
            f"Data Cadastro: {p.data_cadastro}, CPF: {p.cpf}, "
            f"Data Nascimento: {p.data_nascimento}"
        )
