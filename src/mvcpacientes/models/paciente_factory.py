from datetime import date
from mvcpacientes.models.paciente import Paciente


class PacienteFactory:
    """
    Padrão GoF: Factory Method (ou Simple Factory).
    Centraliza a criação de objetos Paciente.
    """

    @staticmethod
    def criar_paciente(
        login: str,
        senha: int,
        nome: str,
        email: str,
        telefone: int,
        cpf: str,
        data_nascimento: str,
        idusuario: int | None = None,
        data_cadastro: date | None = None,
    ) -> Paciente:
        if idusuario is None:
            idusuario = 0  # será preenchido pelo controller depois, se quiser
        if data_cadastro is None:
            data_cadastro = date.today()

        return Paciente(
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
