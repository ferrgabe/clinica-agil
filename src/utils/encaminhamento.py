from datetime import datetime
from typing import List, Optional
import os
import re
import tempfile

from pypdf import PdfMerger  # pip install pypdf
from src.utils.exame import Exame, exportar_exame_pdf


class Encaminhamento:
    def __init__(
        self,
        paciente: str,
        medico_origem: str,
        medico_destino: str,
        motivo: str,
        exames: Optional[List[Exame]] = None
    ):
        
        self.__paciente = None
        self.__medico_origem = None
        self.__medico_destino = None
        self.__motivo = None
        self.__data = datetime.now()
        self.__exames: List[Exame] = []

    @property
    def paciente(self) -> str:
        return self.__paciente

    @paciente.setter
    def paciente(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("O nome do paciente não pode ser vazio.")
        self.__paciente = value.strip()

    @property
    def medico_origem(self) -> str:
        return self.__medico_origem

    @medico_origem.setter
    def medico_origem(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("O médico de origem não pode ser vazio.")
        self.__medico_origem = value.strip()

    @property
    def medico_destino(self) -> str:
        return self.__medico_destino

    @medico_destino.setter
    def medico_destino(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("O médico de destino não pode ser vazio.")
        self.__medico_destino = value.strip()

    @property
    def motivo(self) -> str:
        return self.__motivo

    @motivo.setter
    def motivo(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("O motivo do encaminhamento não pode ser vazio.")
        self.__motivo = value.strip()

    @property
    def data(self) -> datetime:
        return self.__data

    @property
    def exames(self) -> List[Exame]:
        return list(self.__exames)

    def adicionar_exame(self, exame_novo: Exame) -> None:
        if not isinstance(exame_novo, Exame):
            raise TypeError("O objeto deve ser uma instância de Exame.")
        self.__exames.append(exame_novo)

    def __str__(self) -> str:
        exames_str = "\n".join([f"- {exame}" for exame in self.__exames]) if self.__exames else "Nenhum exame encaminhado."
        return (
            f"Encaminhamento:\n"
            f"Paciente: {self.paciente}\n"
            f"Médico de Origem: {self.medico_origem}\n"
            f"Médico de Destino: {self.medico_destino}\n"
            f"Motivo: {self.motivo}\n"
            f"Data: {self.data.strftime('%d/%m/%Y %H:%M')}\n"
            f"Exames Encaminhados:\n{exames_str}"
        )

    # ------ Helpers ------
    @staticmethod
    def _slugify(s: str) -> str:
        s = (s or "").strip().lower()
        s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
        s = re.sub(r"[\s_-]+", "-", s, flags=re.UNICODE)
        s = re.sub(r"^-+|-+$", "", s, flags=re.UNICODE)
        return s or "arquivo"

    # ------ Exportação (PDF único mesclado) ------
    def exportar_pdf_unico(
        self,
        caminho_pdf_unico: str,
        *,
        prefixo_temp: Optional[str] = None,
        titulo_pdf: str = "Relatório de Exame",
        logo_path: Optional[str] = None
    ) -> str:
        """
        Gera um único PDF contendo todos os exames deste encaminhamento, na ordem atual.
        Usa arquivos temporários para cada exame e mescla com pypdf.PdfMerger.

        Retorna: caminho do PDF final gerado.
        """
        if not self.__exames:
            os.makedirs(os.path.dirname(caminho_pdf_unico) or ".", exist_ok=True)
            raise ValueError("Não há exames para exportar.")

        with tempfile.TemporaryDirectory(prefix=(prefixo_temp or "enc-exames-")) as tmpdir:
            temp_paths: List[str] = []
            base = self._slugify(self.paciente) or "encaminhamento"
            data_curta = self.data.strftime("%Y%m%d_%H%M")

            for idx, exame in enumerate(self.__exames, start=1):
                nome_exame_seguro = self._slugify(getattr(exame, "nome", f"exame-{idx}"))
                temp_name = f"{base}_{data_curta}_{idx:02d}_{nome_exame_seguro}.pdf"
                temp_path = os.path.join(tmpdir, temp_name)

                exportar_exame_pdf(
                    exame,
                    temp_path,
                    titulo=titulo_pdf,
                    logo_path=logo_path
                )
                temp_paths.append(temp_path)

            os.makedirs(os.path.dirname(caminho_pdf_unico) or ".", exist_ok=True)
            merger = PdfMerger()
            try:
                for p in temp_paths:
                    merger.append(p)
                merger.write(caminho_pdf_unico)
            finally:
                merger.close()

        return caminho_pdf_unico


def registrar_encaminhamento(paciente, medico_origem, medico_destino, motivo, exames=None):
    encaminhamento = Encaminhamento(paciente, medico_origem, medico_destino, motivo, exames)
    print(encaminhamento)
    return encaminhamento
