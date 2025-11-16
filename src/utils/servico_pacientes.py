from datetime import datetime, date
from typing import Optional

from utils.paciente import Paciente
from utils.interfaces import RepositorioPacientes
from utils.estrategias_listagem import EstrategiaListagem, ListarPorNome


class ServicoPacientes:

    def __init__(self, repositorio: RepositorioPacientes, estrategia: Optional[EstrategiaListagem] = None):
        self.repositorio = repositorio
        # Estratégia padrão: listar por nome
        self.estrategia = estrategia or ListarPorNome()

    # ------------------------
    # VALIDAÇÕES
    # ------------------------
    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        cpf = cpf.strip()
        return cpf.isdigit() and len(cpf) == 11 and cpf != cpf[0] * 11

    @staticmethod
    def validar_data(data_str: str) -> bool:
        try:
            datetime.strptime(data_str, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    # ------------------------
    # CONFIGURAR ESTRATÉGIA (Strategy)
    # ------------------------
    def definir_estrategia_listagem(self, estrategia: EstrategiaListagem) -> None:
        """Troca dinamicamente a forma de ordenar/listar pacientes."""
        self.estrategia = estrategia

    # ------------------------
    # OPERAÇÕES DE NEGÓCIO
    # ------------------------
    def cadastrar(self, login: str, senha: int, nome: str, email: str,
                  telefone: int, cpf: str, data_nascimento: str, tipo: str):

        if not self.validar_cpf(cpf):
            raise ValueError("CPF inválido.")

        if not self.validar_data(data_nascimento):
            raise ValueError("Data de nascimento inválida.")

        # Agora o idusuario NÃO é responsabilidade do serviço.
        # Ele é gerado pelo repositório (PostgreSQL ou memória).
        data_cadastro = date.today()

        paciente = Paciente(
            idusuario=0,  # placeholder; será sobrescrito pelo repositório
            login=login,
            senha=senha,
            nome_completo=nome,
            email=email,
            telefone=telefone,
            data_cadastro=data_cadastro,
            cpf=cpf,
            data_nascimento=data_nascimento,
            tipo=tipo,
        )

        self.repositorio.adicionar(paciente)


    def listar(self):
        """Lista pacientes já aplicando a estratégia de ordenação (Strategy)."""
        pacientes = self.repositorio.listar_todos()
        return self.estrategia.ordenar(pacientes)

    def buscar_por_id(self, idusuario: int):
        return self.repositorio.buscar_por_id(idusuario)
