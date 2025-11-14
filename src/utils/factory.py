from utils.paciente import Paciente
from utils.exame import Exame
from utils.resultado_exame import ResultadoExame
from datetime import date, datetime


class EntidadeFactory:
    @staticmethod
    def criar_paciente(idusuario, login, senha, nome_completo, email, telefone, data_cadastro, cpf, data_nascimento):
        return Paciente(
            idusuario=idusuario,
            login=login,
            senha=senha,
            nome_completo=nome_completo,
            email=email,
            telefone=telefone,
            data_cadastro=data_cadastro,
            cpf=cpf,
            data_nascimento=data_nascimento
        )

    @staticmethod
    def criar_exame(id_exame, nome, tipo):
        return Exame(id_exame=id_exame, nome_exame=nome, tipo_exame=tipo)
    
    @staticmethod
    def criar_resultado_exame(id_resultado, id_exame, data_liberacao, laudo_texto, notificar, paciente):
        return ResultadoExame(id_resultado=id_resultado,
            id_exame=id_exame,
            data_liberacao = data_liberacao,
            laudo_texto = laudo_texto,
            notificar = notificar,  # 0 = não notificar, 1 = SMS, 2 = Email
            paciente = paciente
        )
