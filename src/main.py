from datetime import date
from utils.paciente1 import Paciente
from utils.notificacao import Notificacao


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

    notificacao = Notificacao(
        id_notificacao=1,
        tipo_notificacao=1,
        mensagem="Sua consulta foi confirmada!",
        paciente=paciente1
    )

    status, resposta = notificacao.disparar_sms()
    print("Resposta Twilio:", status, resposta)


if __name__ == "__main__":
    main()