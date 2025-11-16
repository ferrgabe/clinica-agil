from abc import ABC, abstractmethod
from typing import List
from mvcpacientes.models.paciente import Paciente


class EstrategiaListagem(ABC):
    """
    Padrão GoF: STRATEGY
    Define a interface para diferentes formas de ordenar/listar pacientes.
    """

    @abstractmethod
    def ordenar(self, pacientes: List[Paciente]) -> List[Paciente]:
        pass


class ListarPorNome(EstrategiaListagem):
    def ordenar(self, pacientes: List[Paciente]) -> List[Paciente]:
        return sorted(pacientes, key=lambda p: p.nome_completo.lower())


class ListarPorDataCadastro(EstrategiaListagem):
    def ordenar(self, pacientes: List[Paciente]) -> List[Paciente]:
        return sorted(pacientes, key=lambda p: p.data_cadastro)


class ListarPorId(EstrategiaListagem):
    def ordenar(self, pacientes: List[Paciente]) -> List[Paciente]:
        return sorted(pacientes, key=lambda p: p.idusuario)
