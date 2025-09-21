from datetime import date, datetime

class Usuario:
    def __init__(
        self,
        idusuario: int,
        login: str,
        senha: int,
        nome_completo: str,
        email: str,
        telefone: int,
        data_cadastro: date,
    ):
        self.idusuario = idusuario
        self.login = login
        self.senha = senha
        self.nome_completo = nome_completo
        self.email = email
        self.telefone = telefone
        self.data_cadastro = data_cadastro