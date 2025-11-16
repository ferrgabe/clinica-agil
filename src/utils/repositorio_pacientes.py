from typing import List, Optional

from utils.paciente import Paciente
from utils.interfaces import RepositorioPacientes
from utils.repositorio_pacientes_postgres import RepositorioPacientesPostgres


# Implementação concreta do repositório em memória
class RepositorioPacientesMemoria(RepositorioPacientes):

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


# FACTORY METHOD — decide qual repositorio criar
class FabricaRepositorioPacientes:

    @staticmethod
    def criar_repositorio(tipo: str) -> RepositorioPacientes:
        if tipo == "memoria":
            return RepositorioPacientesMemoria()
        elif tipo == "postgres":
            return RepositorioPacientesPostgres()
        else:
            raise ValueError("Tipo de repositório inválido!")
