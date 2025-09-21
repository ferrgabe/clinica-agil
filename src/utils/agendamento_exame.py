class AgendamentoExame:
    def __init__(self, id_agendamento: int, id_exame: int, data_hora: datetime, status: str):
        self.id_agendamento = id_agendamento
        self.id_exame = id_exame
        self.data_hora = data_hora
        self.status = status