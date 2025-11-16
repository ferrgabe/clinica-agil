from datetime import date
from utils.usuario import Usuario  # reaproveita a classe Usuario do projeto


class Paciente(Usuario):
    def __init__(
        self,
        idusuario: int,
        login: str,
        senha: int,
        nome_completo: str,
        email: str,
        telefone: int,
        data_cadastro: date,
        cpf: str,
        data_nascimento: str,
    ):
        super().__init__(
            idusuario=idusuario,
            login=login,
            senha=senha,
            nome_completo=nome_completo,
            email=email,
            telefone=telefone,
            data_cadastro=data_cadastro,
            tipo="paciente",
        )
        self.cpf = cpf
        self.data_nascimento = data_nascimento
