import time
from datetime import date, datetime
from utils.importador_json import ImportadorJSON
from utils.importador_csv import ImportadorCSV
from utils.factory import EntidadeFactory


# ---------------------------------------------------------------
#  Funções do menu
# ---------------------------------------------------------------

def testar_importacao_json():
    exame = EntidadeFactory.criar_exame(
        101,
        "Painel Lipídico",
        "Bioquímica"
    )

    print("\n===== Importação via JSON =====")
    importador = ImportadorJSON()
    importador.importar("utils/dados_exame.json", exame)
    exame.exibir_resultados()

    input("\nPressione ENTER para voltar ao menu...")


def testar_importacao_csv():
    exame = EntidadeFactory.criar_exame(
        102,
        "Painel Renal",
        "Bioquímica"
    )

    print("\n===== Importação via CSV =====")
    importador = ImportadorCSV()
    importador.importar("utils/dados_exame.csv", exame)
    exame.exibir_resultados()

    input("\nPressione ENTER para voltar ao menu...")


def testar_liberacao_resultado():
    paciente1 = EntidadeFactory.criar_paciente(
        1,
        "joaosilva",
        1234,
        "João da Silva",
        "joao@email.com",
        "48996079649",
        date.today(),
        "123.456.789-00",
        date(1990, 5, 10)
    )

    resultado = EntidadeFactory.criar_resultado_exame(
        id_resultado=100,
        id_exame=500,
        data_liberacao=datetime.now(),
        laudo_texto="Exame de sangue: todos os parâmetros normais.",
        notificar=0,  # 1 = SMS
        paciente=paciente1
    )

    print("\n===== Liberando Resultado do Exame =====")
    resultado.liberar_resultado()
    print("\nResultado liberado com sucesso!")

    input("\nPressione ENTER para voltar ao menu...")


# ---------------------------------------------------------------
#  MENU PRINCIPAL
# ---------------------------------------------------------------

def menu():
    while True:
        print("\n======================================")
        print("        SISTEMA CLÍNICA ÁGIL")
        print("======================================")
        print("1 - Importar exame via JSON")
        print("2 - Importar exame via CSV")
        print("3 - Liberar resultado de exame")
        print("0 - Sair")
        print("======================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            testar_importacao_json()

        elif opcao == "2":
            testar_importacao_csv()

        elif opcao == "3":
            testar_liberacao_resultado()

        elif opcao == "0":
            print("\nEncerrando sistema...")
            time.sleep(1)
            break

        else:
            print("\n❌ Opção inválida! Tente novamente.")
            time.sleep(1)


# ---------------------------------------------------------------
#  MAIN
# ---------------------------------------------------------------

if __name__ == "__main__":
    menu()
