import os
import textwrap
import matplotlib.pyplot as plt
from datetime import date, datetime


class Exame:
    def __init__(self, nome, data, resultado):
        self.__nome = nome
        self.__data = data     
        self.__resultado = resultado

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        if not isinstance(value, str):
            raise TypeError("nome deve ser str")
        value = value.strip()
        if not value:
            raise ValueError("nome não pode ser vazio")
        self.__nome = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, str):
            v = value.strip()
            if not v:
                raise ValueError("data não pode ser vazia")
            parsed = None
            for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y"):
                try:
                    parsed = datetime.strptime(v, fmt).date()
                    break
                except ValueError:
                    continue
            if parsed is None:
                raise ValueError("formato de data inválido (use 'DD/MM/AAAA' ou 'YYYY-MM-DD').")
            self.__data = parsed.strftime("%d/%m/%Y")
        elif isinstance(value, datetime):
            self.__data = value.date().strftime("%d/%m/%Y")
        elif isinstance(value, date):
            self.__data = value.strftime("%d/%m/%Y")
        else:
            raise TypeError("data deve ser str, datetime.date ou datetime.datetime")

    @property
    def resultado(self):
        return self.__resultado

    @resultado.setter
    def resultado(self, value):
        if not isinstance(value, str):
            value = str(value)
        value = value.replace("\r\n", "\n").replace("\r", "\n").strip()
        if not value:
            raise ValueError("resultado não pode ser vazio")
        self.__resultado = value

    def __str__(self):
        return (
            f"Exame(nome='{self.__nome}', data='{self.__data}', "
            f"resultado='{(self.__resultado[:40] + '…') if len(self.__resultado) > 43 else self.__resultado}')"
        )

    def __repr__(self):
        return self.__str__()


def exportar_exame_pdf(exame, caminho_pdf, *, titulo="Relatório de Exame", logo_path=None):
    fig = plt.figure(figsize=(8.27, 11.69))  # A4 em polegadas

    left = 0.08
    y = 0.94

    # Título
    fig.text(left, y, titulo, fontsize=18, weight='bold')
    y -= 0.04

    # Logo (opcional)
    if logo_path and os.path.exists(logo_path):
        try:
            ax_logo = fig.add_axes([0.7, 0.90, 0.22, 0.07])
            ax_logo.axis('off')
            ax_logo.imshow(plt.imread(logo_path))
        except Exception:
            pass

    # Linha separadora
    fig.text(left, y, "—" * 80, fontsize=10)
    y -= 0.04

    # Metadados
    fig.text(left, y, f"Nome: {exame.nome}", fontsize=12); y -= 0.03
    fig.text(left, y, f"Data: {exame.data}", fontsize=12); y -= 0.04

    # Resultado (com quebras automáticas)
    fig.text(left, y, "Resultado:", fontsize=12, weight='bold'); y -= 0.03

    max_chars = 100
    wrapped = []
    for paragrafo in str(exame.resultado).split("\n"):
        wrapped.extend(textwrap.wrap(paragrafo, width=max_chars) or [""])
        wrapped.append("")
    if wrapped and wrapped[-1] == "":
        wrapped.pop()

    for line in wrapped:
        if y < 0.06:  # quebra simples de página
            fig.savefig(caminho_pdf, format="pdf", bbox_inches="tight")
            plt.close(fig)
            fig = plt.figure(figsize=(8.27, 11.69))
            left = 0.08
            y = 0.94
            fig.text(left, y, "(continuação)", fontsize=10, style='italic'); y -= 0.04
        fig.text(left, y, line, fontsize=11)

    fig.text(left, 0.04, "Documento gerado automaticamente", fontsize=8, style='italic')
    plt.axis('off')

    os.makedirs(os.path.dirname(caminho_pdf) or ".", exist_ok=True)
    fig.savefig(caminho_pdf, format="pdf", bbox_inches="tight")
    plt.close(fig)

