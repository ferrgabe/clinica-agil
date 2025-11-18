from typing import List, Optional

from mvcpacientes.models.paciente import Paciente
from utils.interfaces import RepositorioPacientes


class RepositorioPacientesMemoria(RepositorioPacientes):
    """
    Implementação concreta do repositório em memória.
    Armazena os pacientes em uma lista na RAM.
    """

    def __init__(self):
        self._lista_pacientes: List[Paciente] = []
        self._proximo_id: int = 1  # contador interno de IDs

    def adicionar(self, paciente: Paciente) -> None:
        # Gera o idusuario automaticamente em memória
        paciente.idusuario = self._proximo_id
        self._proximo_id += 1

        self._lista_pacientes.append(paciente)

    def listar_todos(self) -> List[Paciente]:
        return self._lista_pacientes

    def buscar_por_id(self, idusuario: int) -> Optional[Paciente]:
        for paciente in self._lista_pacientes:
            if paciente.idusuario == idusuario:
                return paciente
        return None
