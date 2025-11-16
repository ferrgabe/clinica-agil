from datetime import date, datetime

from mvcpacientes.models.paciente import Paciente
from mvcpacientes.models.paciente_factory import PacienteFactory
from mvcpacientes.controllers.estrategias_listagem_pacientes import (
    EstrategiaListagemPacientes,
    ListarPacientesPorNome,
    ListarPacientesPorDataCadastro,
)


class PacienteController:
    def __init__(self):
        # Armazena os pacientes em memória
        self._pacientes: list[Paciente] = []
        # Strategy padrão: listar por nome
        self._estrategia_listagem: EstrategiaListagemPacientes = ListarPacientesPorNome()

    # ---------- Validações (regras de negócio) ----------

    def validar_cpf(self, cpf: str) -> bool:
        cpf = cpf.strip()
        return cpf.isdigit() and len(cpf) == 11 and cpf != cpf[0] * 11

    def validar_data(self, data_str: str) -> bool:
        try:
            datetime.strptime(data_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    # ---------- Operações principais ----------

    def proximo_id(self) -> int:
        return len(self._pacientes) + 1

    def cadastrar_paciente(
        self,
        login: str,
        senha: int,
        nome: str,
        email: str,
        telefone: int,
        cpf: str,
        data_nascimento: str,
    ) -> tuple[bool, str]:
        """
        Retorna (sucesso, mensagem).
        Usa Factory para criar o Paciente.
        """

        if not self.validar_cpf(cpf):
            return False, "CPF inválido."

        if not self.validar_data(data_nascimento):
            return False, "Data de nascimento inválida."

        idusuario = self.proximo_id()
        data_cadastro = date.today()

        paciente = PacienteFactory.criar_paciente(
            login=login,
            senha=senha,
            nome=nome,
            email=email,
            telefone=telefone,
            cpf=cpf,
            data_nascimento=data_nascimento,
            idusuario=idusuario,
            data_cadastro=data_cadastro,
        )

        self._pacientes.append(paciente)
        return True, "Paciente cadastrado com sucesso!"

    def listar_pacientes(self) -> list[Paciente]:
        """Lista 'crua', sem ordenação especial (mantida por compatibilidade)."""
        return list(self._pacientes)

    # ---------- Strategy: escolha da forma de listagem ----------

    def definir_estrategia_listagem_por_nome(self) -> None:
        self._estrategia_listagem = ListarPacientesPorNome()

    def definir_estrategia_listagem_por_data_cadastro(self) -> None:
        self._estrategia_listagem = ListarPacientesPorDataCadastro()

    def listar_pacientes_ordenados(self) -> list[Paciente]:
        """Aplica a estratégia de listagem configurada."""
        pacientes = self.listar_pacientes()
        if not pacientes:
            return []
        return self._estrategia_listagem.ordenar(pacientes)
