from datetime import date, datetime
from utils.usuario import Usuario

class Funcionario(Usuario):
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
    ):
        super().__init__(idusuario, login, senha, nome_completo, email, telefone, data_cadastro)
        self.conselho_classe = conselho_classe
        self.registro_classe = registro_classe
        self.cargo = cargo
        self.ativo = ativo