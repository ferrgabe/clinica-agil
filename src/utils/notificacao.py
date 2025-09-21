import requests
from src.utils.paciente import Paciente


class Notificacao:
    def __init__(self, id_notificacao: int, tipo_notificacao: int, mensagem: str, paciente: Paciente):
        self.id_notificacao = id_notificacao
        self.tipo_notificacao = tipo_notificacao
        self.mensagem = mensagem
        self.paciente = paciente 

    def disparar_email(self):
        url = "https://fake.com/api/send_email"  # API fictícia falta implementar orignial
        payload = {
            "to": self.paciente.email,
            "subject": f"Notificação para {self.paciente.nome_completo}",
            "message": self.mensagem,
        }

        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"Email enviado com sucesso para {self.paciente.email}")
        else:
            print(f"Erro ao enviar email: {response.status_code}")
        return response.status_code

    def disparar_sms(self):
        url = "https://fake.com/api/send_sms"  # API fictícia falta implementar orignial
        payload = {
            "to": self.paciente.telefone,
            "message": self.mensagem,
        }

        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"SMS enviado com sucesso para {self.paciente.telefone}")
        else:
            print(f"Erro ao enviar SMS: {response.status_code}")
        return response.status_code
