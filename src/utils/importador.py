from abc import ABC, abstractmethod

class ImportadorBase(ABC):

    def importar(self, caminho_arquivo: str, exame):
        dados = self.ler_arquivo(caminho_arquivo)
        if not self.validar(dados):
            raise ValueError("Dados inválidos ou corrompidos.")
        resultados = self.processar(dados)

        # Chama exame, passa os resultados lidos
        exame.receber_resultados_importados(resultados)
        self.salvar(resultados)
        print("*** Importação concluída! ***")
        return resultados

    @abstractmethod
    def ler_arquivo(self, caminho_arquivo: str):
        pass

    @abstractmethod
    def validar(self, dados):
        pass

    @abstractmethod
    def processar(self, dados):
        pass

    def salvar(self, resultados):
        print(f"{len(resultados)} resultados processados.\n")
