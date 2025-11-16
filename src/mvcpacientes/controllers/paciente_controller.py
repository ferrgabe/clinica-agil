from datetime import date, datetime
from mvcpacientes.models.paciente import Paciente


class PacienteController:
    def __init__(self):
        # Aqui vamos manter os pacientes em memória
        self._pacientes: list[Paciente] = []

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
        Não usa input()/print(), só regra de negócio.
        """

        if not self.validar_cpf(cpf):
            return False, "CPF inválido."

        if not self.validar_data(data_nascimento):
            return False, "Data de nascimento inválida."

        idusuario = self.proximo_id()
        data_cadastro = date.today()

        paciente = Paciente(
            idusuario=idusuario,
            login=login,
            senha=senha,
            nome_completo=nome,
            email=email,
            telefone=telefone,
            data_cadastro=data_cadastro,
            cpf=cpf,
            data_nascimento=data_nascimento,
        )
        self._pacientes.append(paciente)
        return True, "Paciente cadastrado com sucesso!"

    def listar_pacientes(self) -> list[Paciente]:
        # Devolve uma cópia da lista para não deixarem mexer direto
        return list(self._pacientes)
