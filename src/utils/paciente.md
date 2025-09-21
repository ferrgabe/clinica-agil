## Nota: Guilherme Hino
Inicializador da classe Paciente, não editei o arquivo paciente.py antes pra não dar conflito.

from datetime import date, datetime
from typing import List

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
        data_nascimento: date,
        sexo: str,
        historico_medico: List[str],
    ):
        super().__init__(idusuario, login, senha, nome_completo, email, telefone, data_cadastro)
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.historico_medico = historico_medico