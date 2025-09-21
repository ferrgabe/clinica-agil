from datetime import datetime

pacientes = []

def validar_cpf(cpf):
    cpf = cpf.strip()
    return cpf.isdigit() and len(cpf) == 11 and cpf != cpf[0] * 11

def validar_data(data_str):
    try:
        datetime.strptime(data_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def cadastrar_paciente():
    print("=== Cadastro de Paciente ===")
    nome = input("Nome completo: ")
    cpf = input("CPF (somente números): ")
    if not validar_cpf(cpf):
        print("CPF inválido.")
        return
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    if not validar_data(data_nascimento):
        print("Data de nascimento inválida.")
        return
    paciente = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento
    }
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

def listar_pacientes():
    print("\nPacientes cadastrados:")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    for p in pacientes:
        print(f"Nome: {p['nome']}, CPF: {p['cpf']}, Data de Nascimento: {p['data_nascimento']}")

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1 - Cadastrar paciente")
        print("2 - Listar pacientes")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_paciente()
        elif opcao == '2':
            listar_pacientes()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")