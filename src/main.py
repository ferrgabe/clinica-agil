from datetime import date
from utils.paciente1 import Paciente
from utils.medico import Medico
from utils.secretaria import Secretaria
from utils.tecnico_responsavel import TecnicoResponsavel
from utils.notificacao import Notificacao
from utils.usuario import Usuario

#Isso aqui é o main real
def main():
    paciente1 = Paciente(
        idusuario=1,
        login="joaosilva",
        senha=1234,
        nome_completo="João da Silva",
        email="joao@email.com",
        telefone="48996079649",  # apenas números, o código adiciona +55
        data_cadastro=date.today(),
        cpf="123.456.789-00",
        data_nascimento=date(1990, 5, 10),
        sexo="M",
        historico_medico=[]
    )

    medico1 = Medico(
        idusuario=2,
        login="drmaria",
        senha=4321,
        nome_completo="Dra. Maria Oliveira",
        email="maria@hospital.com",
        telefone="48999998888",
        data_cadastro=date.today(),
        conselho_classe="CRM",
        registro_classe="12345-SC",
        cargo="Médica",
        ativo=True,
        especialidade="Cardiologia"
    )

    secretaria1 = Secretaria(
        idusuario=3,
        login="ana_secretaria",
        senha=1111,
        nome_completo="Ana Souza",
        email="ana@hospital.com",
        telefone="48988887777",
        data_cadastro=date.today(),
        conselho_classe="COREN",
        registro_classe="54321-SC",
        cargo="Secretária",
        ativo=True
    )

    tecnico1 = TecnicoResponsavel(
        idusuario=4,
        login="enf_carlos",
        senha=2222,
        nome_completo="Carlos Almeida",
        email="carlos@hospital.com",
        telefone="48997776655",
        data_cadastro=date.today(),
        conselho_classe="COFEN",
        registro_classe="67890-SC",
        cargo="Enfermeiro",
        ativo=True,
        especializacao="Enfermagem Intensiva"
    )

    lista_usuarios = [paciente1, medico1, secretaria1, tecnico1]

    # Teste de Login
    usuario_logado = Usuario.login(lista_usuarios, "enf_carlos", 2222)

    if usuario_logado:
        print(f"Usuário autenticado com sucesso: {usuario_logado.nome_completo}")
        print("Tipo de usuário:", usuario_logado.__class__.__name__)
    else:
        print("Falha na autenticação: login ou senha incorretos.")

    notificacao = Notificacao(
        id_notificacao=1,
        tipo_notificacao=1,
        mensagem="Sua consulta foi confirmada!",
        paciente=paciente1
    )

    status, resposta = notificacao.disparar_sms()
    print("Resposta Twilio:", status, resposta)

# #Teste - Ignorar
# def criar_usuarios_teste():
#     paciente1 = Paciente(
#         idusuario=1,
#         login="joaosilva",
#         senha=1234,
#         nome_completo="João da Silva",
#         email="joao@email.com",
#         telefone="48996079649",
#         data_cadastro=date.today(),
#         cpf="12345678900",
#         data_nascimento=date(1990, 5, 10),
#         sexo="M",
#         historico_medico=[]
#     )

#     medico1 = Medico(
#         idusuario=2,
#         login="drmaria",
#         senha=4321,
#         nome_completo="Dra. Maria Oliveira",
#         email="maria@hospital.com",
#         telefone="48999998888",
#         data_cadastro=date.today(),
#         conselho_classe="CRM",
#         registro_classe="12345-SC",
#         cargo="Médica",
#         ativo=True,
#         especialidade="Cardiologia"
#     )

#     secretaria1 = Secretaria(
#         idusuario=3,
#         login="ana_secretaria",
#         senha=1111,
#         nome_completo="Ana Souza",
#         email="ana@hospital.com",
#         telefone="48988887777",
#         data_cadastro=date.today(),
#         conselho_classe="COREN",
#         registro_classe="54321-SC",
#         cargo="Secretária",
#         ativo=True
#     )

#     tecnico1 = TecnicoResponsavel(
#         idusuario=4,
#         login="enf_carlos",
#         senha=2222,
#         nome_completo="Carlos Almeida",
#         email="carlos@hospital.com",
#         telefone="48997776655",
#         data_cadastro=date.today(),
#         conselho_classe="COFEN",
#         registro_classe="67890-SC",
#         cargo="Enfermeiro",
#         ativo=True,
#         especializacao="Enfermagem Intensiva"
#     )

#     return [paciente1, medico1, secretaria1, tecnico1]

# #Teste - Ignorar
# def testar_login():
#     lista_usuarios = criar_usuarios_teste()

#     print("=== Teste de Login ===")
#     login_input = input("Digite login ou email: ")
#     senha_input = int(input("Digite senha: "))

#     status, mensagem, usuario_logado = Usuario.login(lista_usuarios, login_input, senha_input)

#     print(mensagem)
#     if status:
#         print("Usuário autenticado é do tipo:", usuario_logado.__class__.__name__)
#     else:
#         print("Falha no login.")


if __name__ == "__main__":
    main()

# #Teste - Ignorar
# if __name__ == "__main__":
#     testar_login()