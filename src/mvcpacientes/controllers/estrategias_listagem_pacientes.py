from abc import ABC, abstractmethod
from mvcpacientes.models.paciente import Paciente


class EstrategiaListagemPacientes(ABC):
    """
    Padrão GoF: Strategy.
    Define a interface para estratégias de ordenação de pacientes.
    """

    @abstractmethod
    def ordenar(self, pacientes: list[Paciente]) -> list[Paciente]:
        """Recebe a lista de pacientes e retorna uma nova lista ordenada."""
        raise NotImplementedError


class ListarPacientesPorNome(EstrategiaListagemPacientes):
    def ordenar(self, pacientes: list[Paciente]) -> list[Paciente]:
        return sorted(pacientes, key=lambda p: p.nome_completo.lower())


class ListarPacientesPorDataCadastro(EstrategiaListagemPacientes):
    def ordenar(self, pacientes: list[Paciente]) -> list[Paciente]:
        return sorted(pacientes, key=lambda p: p.data_cadastro)
