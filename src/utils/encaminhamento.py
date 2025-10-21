from datetime import datetime
from src.utils.exame import Exame  
from typing import List

class Encaminhamento:
    def __init__(self, paciente, medico_origem, medico_destino, motivo, exames=None):
        self.paciente = paciente
        self.medico_origem = medico_origem
        self.medico_destino = medico_destino
        self.motivo = motivo
        self.data = datetime.now()
        self.exames: List[exame] = exames if exames is not None else []

    def adicionar_exame(self, exame_novo: Exame) -> None:
 
        self.exames.append(exame_novo)

    def __str__(self):
        exames_str = "\n".join([f"- {exame}" for exame in self.exames]) if self.exames else "Nenhum exame encaminhado."
        return (
            f"Encaminhamento:\n"
            f"Paciente: {self.paciente}\n"
            f"Médico de Origem: {self.medico_origem}\n"
            f"Médico de Destino: {self.medico_destino}\n"
            f"Motivo: {self.motivo}\n"
            f"Data: {self.data.strftime('%d/%m/%Y %H:%M')}\n"
            f"Exames Encaminhados:\n{exames_str}"
        )
        
def registrar_encaminhamento(paciente, medico_origem, medico_destino, motivo, exames=None):
    encaminhamento = Encaminhamento(paciente, medico_origem, medico_destino, motivo, exames)
    print(encaminhamento)
    return encaminhamento
