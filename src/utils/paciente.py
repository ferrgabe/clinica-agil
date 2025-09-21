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

if __name__ == "__main__":
    while True:
        cadastrar_paciente()
        cont = input("Deseja cadastrar outro paciente? (s/n): ")
        if cont.lower() != 's':
            break
    print("\nPacientes cadastrados:")
    for p in pacientes:
        print(p)