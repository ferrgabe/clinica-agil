from datetime import datetime
from utils.notificacao import Notificacao
from utils.paciente import Paciente


class ResultadoExame:
    def __init__(
        self,
        id_resultado: int,
        id_exame: int,
        data_liberacao: datetime,
        laudo_texto: str,
        notificar: int,
        paciente: Paciente
    ):
        self.id_resultado = id_resultado
        self.id_exame = id_exame
        self.data_liberacao = data_liberacao
        self.laudo_texto = laudo_texto
        self.notificar = notificar  # 0 = não notificar, 1 = SMS, 2 = Email
        self.paciente = paciente

    def liberar_resultado(self):
        self.data_liberacao = datetime.now()
        print(f"Resultado do exame {self.id_exame} liberado em {self.data_liberacao}")
        print(f"Laudo: {self.laudo_texto}")
        # IMPORTANTE: Incluir o armazenamento no BD nesta etapa

        if self.notificar != 0:
            self.enviar_notificacao()

    def enviar_notificacao(self):
        mensagem = f"Olá {self.paciente.nome_completo}, seu exame realizado na Clinica Agil está disponível."
        notificacao = Notificacao(
            id_notificacao=self.id_resultado,
            tipo_notificacao=self.notificar,
            mensagem=mensagem,
            paciente=self.paciente
        )
        print(notificacao)

        if self.notificar == 1:
            notificacao.disparar_sms()
        elif self.notificar == 2:
            notificacao.disparar_email()
        else:
            print("Tipo de notificação inválido.")

    def visualizar_resultado(self):
        return {
            "id_resultado": self.id_resultado,
            "id_exame": self.id_exame,
            "data_liberacao": self.data_liberacao.strftime("%d/%m/%Y %H:%M:%S"),
            "laudo_texto": self.laudo_texto,
            "paciente": self.paciente.nome_completo,
        }
