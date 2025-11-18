import json
import os
from datetime import date
from typing import List, Optional

from mvcpacientes.models.paciente import Paciente
from utils.interfaces import RepositorioPacientes


class RepositorioPacientesJSON(RepositorioPacientes):
    """
    Implementação de RepositorioPacientes que salva os dados
    em um arquivo JSON (pacientes.json).
    """

    def __init__(self, caminho_arquivo: str = "pacientes.json"):
        self.caminho_arquivo = caminho_arquivo

        # Garante que o arquivo existe
        if not os.path.exists(self.caminho_arquivo):
            with open(self.caminho_arquivo, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)

        # Define o próximo id com base no que já existe no arquivo
        dados = self._carregar_dados_brutos()
        if dados:
            self._proximo_id = max(item.get("idusuario", 0) for item in dados) + 1
        else:
            self._proximo_id = 1

    # ---------- Métodos internos de apoio ----------

    def _carregar_dados_brutos(self) -> list:
        try:
            with open(self.caminho_arquivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _salvar_dados_brutos(self, dados: list) -> None:
        with open(self.caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

    def _dict_para_paciente(self, dado: dict) -> Paciente:
        """
        Converte um dicionário (do JSON) em um objeto Paciente.
        """
        data_cadastro_str = dado.get("data_cadastro")
        if isinstance(data_cadastro_str, str):
            data_cadastro = date.fromisoformat(data_cadastro_str)
        else:
            # fallback: hoje, se por algum motivo vier errado
            data_cadastro = date.today()

        return Paciente(
            idusuario=dado.get("idusuario"),
            login=dado.get("login", ""),
            senha=dado.get("senha", ""),
            nome_completo=dado.get("nome_completo", ""),
            email=dado.get("email", ""),
            telefone=dado.get("telefone", ""),
            data_cadastro=data_cadastro,
            cpf=dado.get("cpf", ""),
            data_nascimento=dado.get("data_nascimento", ""),
            tipo=dado.get("tipo", "paciente"),
        )

    def _paciente_para_dict(self, paciente: Paciente) -> dict:
        """
        Converte um objeto Paciente em um dicionário serializável em JSON.
        """
        return {
            "idusuario": paciente.idusuario,
            "login": paciente.login,
            "senha": paciente.senha,
            "nome_completo": paciente.nome_completo,
            "email": paciente.email,
            "telefone": paciente.telefone,
            "data_cadastro": paciente.data_cadastro.isoformat()
            if isinstance(paciente.data_cadastro, date)
            else str(paciente.data_cadastro),
            "cpf": paciente.cpf,
            "data_nascimento": paciente.data_nascimento,
            "tipo": paciente.tipo,
        }

    # ---------- Implementação da interface RepositorioPacientes ----------

    def adicionar(self, paciente: Paciente) -> None:
        dados = self._carregar_dados_brutos()

        # Gera ID novo sempre pelo repositório (como na memória)
        paciente.idusuario = self._proximo_id
        self._proximo_id += 1

        dados.append(self._paciente_para_dict(paciente))
        self._salvar_dados_brutos(dados)

    def listar_todos(self) -> List[Paciente]:
        dados = self._carregar_dados_brutos()
        return [self._dict_para_paciente(item) for item in dados]

    def buscar_por_id(self, idusuario: int) -> Optional[Paciente]:
        dados = self._carregar_dados_brutos()
        for item in dados:
            if item.get("idusuario") == idusuario:
                return self._dict_para_paciente(item)
        return None
