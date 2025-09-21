import requests
import os
from utils.paciente1 import Paciente
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

class Notificacao:
    def __init__(self, id_notificacao: int, tipo_notificacao: int, mensagem: str, paciente: Paciente):
        self.id_notificacao = id_notificacao
        self.tipo_notificacao = tipo_notificacao
        self.mensagem = mensagem
        self.paciente = paciente 

        self.account_sid = os.getenv("SMS_ACCOUNT_SID")
        self.auth_token = os.getenv("SMS_AUTH_TOKEN")
        self.messaging_service_sid = os.getenv("SMS_MESSAGING_SERVICE_SID")

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
        url = f"https://api.twilio.com/2010-04-01/Accounts/{self.account_sid}/Messages.json"
        payload = {
            "To": f"+55{self.paciente.telefone}",
            "MessagingServiceSid": self.messaging_service_sid,
            "Body": self.mensagem,
        }

        response = requests.post(url, data=payload, auth=(self.account_sid, self.auth_token))

        if response.status_code == 201:
            print(f"SMS enviado com sucesso para {self.paciente.telefone}")
        else:
            print(f"Erro ao enviar SMS: {response.status_code}, {response.text}")

        return response.status_code, response.text
