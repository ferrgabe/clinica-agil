from datetime import date, datetime

class ResultadoExame:
    def __init__(self, id_resultado: int, id_exame: int, data_liberacao: datetime, laudo_texto: str):
        self.id_resultado = id_resultado
        self.id_exame = id_exame
        self.data_liberacao = data_liberacao
        self.laudo_texto = laudo_texto