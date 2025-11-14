import csv
from utils.importador import ImportadorBase
import time

class ImportadorCSV(ImportadorBase):
    def ler_arquivo(self, caminho_arquivo: str):
        print(f"...Lendo CSV: {caminho_arquivo}")
        time.sleep(1)
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            return list(csv.DictReader(f))
        
    def validar(self, dados):
        print("...Validando dados CSV...")
        time.sleep(1)
        return all("parametro" in linha for linha in dados)

    def processar(self, dados):
        print("...Processando CSV...")
        time.sleep(1)
        return dados
