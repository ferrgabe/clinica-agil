from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import date

class RepositorioPacientes(ABC):

    @abstractmethod
    def adicionar(self, paciente):
        pass

    @abstractmethod
    def listar_todos(self) -> List:
        pass

    @abstractmethod
    def buscar_por_id(self, idusuario: int):
        pass
