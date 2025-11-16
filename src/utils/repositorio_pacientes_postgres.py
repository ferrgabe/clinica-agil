import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import date
from typing import List, Optional

from utils.paciente import Paciente
from utils.interfaces import RepositorioPacientes


class RepositorioPacientesPostgres(RepositorioPacientes):

    def __init__(self, host="localhost", database="clinica_agil", user="postgres", password="321gui321"):
        self.conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        self.conn.autocommit = True

    def adicionar(self, paciente: Paciente) -> None:
        """
        Adiciona o paciente no banco.
        O idusuario é gerado automaticamente pelo PostgreSQL (sequence).
        """
        with self.conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO pacientes (
                    login,
                    senha,
                    nome_completo,
                    email,
                    telefone,
                    data_cadastro,
                    cpf,
                    data_nascimento,
                    tipo
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING idusuario
                """,
                (
                    paciente.login,
                    paciente.senha,
                    paciente.nome_completo,
                    paciente.email,
                    paciente.telefone,
                    paciente.data_cadastro,
                    paciente.cpf,
                    paciente.data_nascimento,
                    paciente.tipo,
                )
            )
            novo_id = cur.fetchone()[0]
            paciente.idusuario = novo_id


    def listar_todos(self) -> List[Paciente]:
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM pacientes ORDER BY idusuario")
            linhas = cur.fetchall()

        pacientes = []
        for row in linhas:
            pacientes.append(
                Paciente(
                    row["idusuario"],
                    row["login"],
                    row["senha"],
                    row["nome_completo"],
                    row["email"],
                    row["telefone"],
                    row["data_cadastro"],
                    row["cpf"],
                    row["data_nascimento"],
                    row["tipo"]
                )
            )
        return pacientes

    def buscar_por_id(self, idusuario: int) -> Optional[Paciente]:
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM pacientes WHERE idusuario = %s", (idusuario,))
            row = cur.fetchone()

        if not row:
            return None

        return Paciente(
            row["idusuario"],
            row["login"],
            row["senha"],
            row["nome_completo"],
            row["email"],
            row["telefone"],
            row["data_cadastro"],
            row["cpf"],
            row["data_nascimento"],
            row["tipo"]
        )

