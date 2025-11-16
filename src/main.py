import time
from datetime import date, datetime
from utils.importador_json import ImportadorJSON
from utils.importador_csv import ImportadorCSV
from utils.factory import EntidadeFactory
from utils.repositorio_pacientes import FabricaRepositorioPacientes
from utils.servico_pacientes import ServicoPacientes
from utils.estrategias_listagem import ListarPorNome, ListarPorDataCadastro, ListarPorId


1
# Instâncias globais para o módulo de Pacientes
repositorio_pacientes = FabricaRepositorioPacientes.criar_repositorio("postgres")
servico_pacientes = ServicoPacientes(repositorio_pacientes)




# ---------------------------------------------------------------
#  Funções do menu
# ---------------------------------------------------------------

def testar_importacao_json():
    exame = EntidadeFactory.criar_exame(
        101,
        "Painel Lipídico",
        "Bioquímica"
    )

    print("\n===== Importação via JSON =====")
    importador = ImportadorJSON()
    importador.importar("utils/dados_exame.json", exame)
    exame.exibir_resultados()

    input("\nPressione ENTER para voltar ao menu...")


def testar_importacao_csv():
    exame = EntidadeFactory.criar_exame(
        102,
        "Painel Renal",
        "Bioquímica"
    )

    print("\n===== Importação via CSV =====")
    importador = ImportadorCSV()
    importador.importar("utils/dados_exame.csv", exame)
    exame.exibir_resultados()

    input("\nPressione ENTER para voltar ao menu...")


def testar_liberacao_resultado():
    paciente1 = EntidadeFactory.criar_paciente(
        1,
        "joaosilva",
        1234,
        "João da Silva",
        "joao@email.com",
        "48996079649",
        date.today(),
        "123.456.789-00",
        date(1990, 5, 10)
    )

    resultado = EntidadeFactory.criar_resultado_exame(
        id_resultado=100,
        id_exame=500,
        data_liberacao=datetime.now(),
        laudo_texto="Exame de sangue: todos os parâmetros normais.",
        notificar=0,  # 1 = SMS
        paciente=paciente1
    )

    print("\n===== Liberando Resultado do Exame =====")
    resultado.liberar_resultado()
    print("\nResultado liberado com sucesso!")

    input("\nPressione ENTER para voltar ao menu...")

#guilherme hino início

def escolher_estrategia_pacientes():
    print("\n=== Estratégia de listagem de pacientes (Strategy) ===")
    print("1 - Listar por NOME (A-Z)")
    print("2 - Listar por DATA DE CADASTRO (mais antigos primeiro)")
    print("3 - Listar por ID")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        servico_pacientes.definir_estrategia_listagem(ListarPorNome())
        print("Estratégia alterada para: NOME (A-Z).")
    elif opcao == "2":
        servico_pacientes.definir_estrategia_listagem(ListarPorDataCadastro())
        print("Estratégia alterada para: DATA DE CADASTRO.")
    elif opcao == "3":
        servico_pacientes.definir_estrategia_listagem(ListarPorId())
        print("Estratégia alterada para: ID.")
    else:
        print("Opção inválida. Mantendo a estratégia atual.")

    input("\nPressione ENTER para voltar ao menu de pacientes...")


def cadastrar_paciente_via_input():
    print("\n=== Cadastro de Paciente ===")
    login = input("Login: ")
    senha = int(input("Senha (apenas números): "))
    nome = input("Nome completo: ")
    email = input("Email: ")
    telefone = int(input("Telefone (apenas números): "))
    cpf = input("CPF (somente números): ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    tipo = input("Tipo (ex: 'paciente'): ")

    try:
        servico_pacientes.cadastrar(
            login=login,
            senha=senha,
            nome=nome,
            email=email,
            telefone=telefone,
            cpf=cpf,
            data_nascimento=data_nascimento,
            tipo=tipo,
        )
        print("\nPaciente cadastrado com sucesso!")
    except ValueError as e:
        print(f"\nErro ao cadastrar paciente: {e}")

    input("\nPressione ENTER para voltar ao menu de pacientes...")


def listar_pacientes():
    print("\n=== Lista de Pacientes (aplicando Strategy) ===")
    pacientes = servico_pacientes.listar()
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        for p in pacientes:
            print(
                f"ID: {p.idusuario}, "
                f"Login: {p.login}, "
                f"Nome: {p.nome_completo}, "
                f"Email: {p.email}, "
                f"Telefone: {p.telefone}, "
                f"Data Cadastro: {p.data_cadastro}, "
                f"CPF: {p.cpf}, "
                f"Data Nascimento: {p.data_nascimento}, "
                f"Tipo: {p.tipo}"
            )

    input("\nPressione ENTER para voltar ao menu de pacientes...")


def menu_pacientes():
    while True:
        print("\n===== MÓDULO DE PACIENTES (GoF) =====")
        print("1 - Cadastrar paciente")
        print("2 - Listar pacientes")
        print("3 - Trocar estratégia de listagem (Strategy)")
        print("0 - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente_via_input()
        elif opcao == "2":
            listar_pacientes()
        elif opcao == "3":
            escolher_estrategia_pacientes()
        elif opcao == "0":
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")
            time.sleep(1)

#guilherme hino fim


# ---------------------------------------------------------------
#  MENU PRINCIPAL
# ---------------------------------------------------------------

def menu():
    while True:
        print("\n======================================")
        print("        SISTEMA CLÍNICA ÁGIL")
        print("======================================")
        print("1 - Importar exame via JSON")
        print("2 - Importar exame via CSV")
        print("3 - Liberar resultado de exame")
        print("4 - Módulo de Pacientes (GoF)") #guilherme hino adição
        print("0 - Sair")
        print("======================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            testar_importacao_json()

        elif opcao == "2":
            testar_importacao_csv()

        elif opcao == "3":
            testar_liberacao_resultado()

        elif opcao == "4":
            menu_pacientes()
        
        elif opcao == "0":
            print("\nEncerrando sistema...")
            time.sleep(1)
            break

        else:
            print("\n❌ Opção inválida! Tente novamente.")
            time.sleep(1)


# ---------------------------------------------------------------
#  MAIN
# ---------------------------------------------------------------

if __name__ == "__main__":
    menu()