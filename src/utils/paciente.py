from datetime import date
from utils.usuario import Usuario

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
        tipo: str
    ):
        super().__init__(idusuario, login, senha, nome_completo, email, telefone, data_cadastro, tipo)
        self.cpf = cpf
        self.data_nascimento = data_nascimento
