from datetime import date, datetime
from src.utils.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(
        self,
        idusuario: int,
        login: str,
        senha: int,
        nome_completo: str,
        email: str,
        telefone: int,
        data_cadastro: date,
        conselho_classe: str,
        registro_classe: str,
        cargo: str,
        ativo: bool,
        especialidade: str,
    ):
        super().__init__(idusuario, login, senha, nome_completo, email, telefone, data_cadastro,
                         conselho_classe, registro_classe, cargo, ativo)
        self.especialidade = especialidade