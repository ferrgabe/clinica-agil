import json
from utils.importador import ImportadorBase
import time

class ImportadorJSON(ImportadorBase):
    def ler_arquivo(self, caminho_arquivo: str):
        print(f"...Lendo JSON: {caminho_arquivo}")
        time.sleep(1)
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            return json.load(f)

    def validar(self, dados):
        print("...Validando dados JSON...")
        time.sleep(1)
        return "resultados" in dados and isinstance(dados["resultados"], list)

    def processar(self, dados):
        print("...Processando dados JSON...")
        time.sleep(1)
        return dados["resultados"]
