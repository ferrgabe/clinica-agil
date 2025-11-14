import os
import json
import textwrap
import matplotlib.pyplot as plt
from datetime import date, datetime


class Exame:
    def __init__(self, id_exame: int, nome_exame: str, tipo_exame: str):
        self.id_exame = id_exame
        self.nome_exame = nome_exame
        self.tipo_exame = tipo_exame
        self.resultados = []
        self.data_importacao = None


        self.__data = None
        self.__resultado = None         # texto livre p/ PDF

    # ------------------------------------------------------------
    # PROPRIEDADES — versão do Hino
    # ------------------------------------------------------------

    @property
    def nome_exame(self):
        return self.__nome

    @nome_exame.setter
    def nome_exame(self, value):
        if not isinstance(value, str):
            raise TypeError("nome_exame deve ser str")
        v = value.strip()
        if not v:
            raise ValueError("nome_exame não pode ser vazio")
        self.__nome = v

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
                raise ValueError("Formato de data inválido. Use DD/MM/AAAA.")
            self.__data = parsed.strftime("%d/%m/%Y")

        elif isinstance(value, (date, datetime)):
            self.__data = value.strftime("%d/%m/%Y")
        else:
            raise TypeError("data deve ser str, date ou datetime")

    @property
    def resultado(self):
        return self.__resultado

    @resultado.setter
    def resultado(self, value):
        if not isinstance(value, str):
            value = str(value)

        v = value.replace("\r\n", "\n").replace("\r", "\n").strip()
        if not v:
            raise ValueError("resultado não pode ser vazio")

        self.__resultado = v

    # ------------------------------------------------------------
    # IMPORTAÇÃO — parte do Gabe, usando Template Method
    # ------------------------------------------------------------

    def receber_resultados_importados(self, resultados):
        self.data_importacao = datetime.now()
        self.resultados = []

        for item in resultados:
            self.resultados.append({
                "parametro": item.get("parametro"),
                "valor": item.get("valor"),
                "unidade": item.get("unidade"),
                "referencia": item.get("referencia"),
                "status": item.get("status")
            })

        print(f"Dados entregues ao exame {self.nome_exame} com sucesso!")

    # ------------------------------------------------------------
    # VISUALIZAÇÃO — Gabe
    # ------------------------------------------------------------

    def exibir_resultados(self):
        print(f"\nResultados do exame: {self.nome_exame} (ID: {self.id_exame})")
        print(f"Tipo: {self.tipo_exame}")
        print(f"Data da importação: {self.data_importacao.strftime('%d/%m/%Y %H:%M:%S') if self.data_importacao else 'N/A'}")
        print("-" * 60)

        for r in self.resultados:
            print(
                f"{r['parametro']:<25} "
                f"{r['valor']:<10} {r['unidade']:<6} "
                f"Ref: {r['referencia']:<15} Status: {r['status']}"
            )

        print("-" * 60)

    # ------------------------------------------------------------
    # EXPORTAÇÃO em Json - Gabe
    # ------------------------------------------------------------

    def exportar_resultados(self):
        return json.dumps({
            "id_exame": self.id_exame,
            "nome_exame": self.nome_exame,
            "tipo_exame": self.tipo_exame,
            "data_importacao": self.data_importacao.strftime("%Y-%m-%d %H:%M:%S") if self.data_importacao else None,
            "resultados": self.resultados
        }, indent=4, ensure_ascii=False)

    # ------------------------------------------------------------
    # EXPORTAÇÃO PDF — Hino
    # ------------------------------------------------------------

    def exportar_pdf(self, caminho_pdf, *, titulo="Relatório de Exame", logo_path=None):
        fig = plt.figure(figsize=(8.27, 11.69))

        left = 0.08
        y = 0.94

        fig.text(left, y, titulo, fontsize=18, weight='bold')
        y -= 0.04

        if logo_path and os.path.exists(logo_path):
            try:
                ax_logo = fig.add_axes([0.7, 0.90, 0.22, 0.07])
                ax_logo.axis('off')
                ax_logo.imshow(plt.imread(logo_path))
            except Exception:
                pass

        fig.text(left, y, "—" * 80, fontsize=10)
        y -= 0.04

        fig.text(left, y, f"Nome: {self.nome_exame}", fontsize=12); y -= 0.03
        fig.text(left, y, f"Data: {self.data}", fontsize=12); y -= 0.04

        fig.text(left, y, "Resultado:", fontsize=12, weight='bold'); y -= 0.03

        max_chars = 100
        wrapped = []
        for paragrafo in str(self.resultado).split("\n"):
            wrapped.extend(textwrap.wrap(paragrafo, width=max_chars) or [""])
            wrapped.append("")

        if wrapped and wrapped[-1] == "":
            wrapped.pop()

        for line in wrapped:
            if y < 0.06:
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
