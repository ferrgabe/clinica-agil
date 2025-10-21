from datetime import datetime, date
from usuario import Usuario

class Paciente(Usuario):
    def __init__(self, idusuario: int, login: str, senha: int, nome_completo: str, email: str, telefone: int, data_cadastro: date, cpf: str, data_nascimento: str):
        super().__init__(idusuario, login, senha, nome_completo, email, telefone, data_cadastro)
        self.cpf = cpf
        self.data_nascimento = data_nascimento

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

def # The `cadastrar_paciente()` function is responsible for registering a new patient in the system.
# It prompts the user to input various details such as login, password, name, email, phone number,
# CPF (Brazilian individual taxpayer registry identification), and date of birth.
cadastrar_paciente():
    print("=== Cadastro de Paciente ===")
    idusuario = len(pacientes) + 1
    login = input("Login: ")
    senha = int(input("Senha (apenas números): "))
    nome = input("Nome completo: ")
    email = input("Email: ")
    telefone = int(input("Telefone (apenas números): "))
    data_cadastro = date.today()
    cpf = input("CPF (somente números): ")
    if not validar_cpf(cpf):
        print("CPF inválido.")
        return
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    if not validar_data(data_nascimento):
        print("Data de nascimento inválida.")
        return
    paciente = Paciente(
        idusuario, login, senha, nome, email, telefone, data_cadastro, cpf, data_nascimento
    )
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

def listar_pacientes():
    print("\nPacientes cadastrados:")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    for p in pacientes:
        print(f"ID: {p.idusuario}, Login: {p.login}, Nome: {p.nome_completo}, Email: {p.email}, Telefone: {p.telefone}, Data Cadastro: {p.data_cadastro}, CPF: {p.cpf}, Data de Nascimento: {p.data_nascimento}")

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
