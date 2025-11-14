# Projeto da clinica agil, desenvolvido para a disciplina de Engenharia de Software I 25.2

### Autores: Roberto Ferreira; Adan Pruss; Guilherme Drummond; Guilherme Hino

Explicação parte do Roberto Ferreira:

1. Implementei o GoF **Template Method** na classe importador.py, ele funciona como um template geral para as classes filhas JSON e CSV (podendo ser estendida para XML, FHIR se necessário).
   Utiliza princípios de OO como Herança, Polimorfismo e Encapsulamento. O encapsulamento pode ser visto no trecho abaixo, onde a chamada .importar "chama o método importar da classe Mãe:

````python
importador = ImportadorCSV()
importador.importar("utils/dados_exame.csv", exame)
````


2. Implementei também o **Factory** no projeto geral, é possível observar que todas as instanciações estão sendo feitas na chamada da função criar_xxxx da classe EntidadeFactory.
É mais fácil de gerenciar os imports, visto que só preciso importar o factory ao invés de cada classe

````python
    exame = EntidadeFactory.criar_exame(
        102,
        "Painel Renal",
        "Bioquímica"
    )
````

3. UC 08. Notificar liberação de resultados.

- Permanece semelhante a ultima versão, no entanto a responsabilidade da liberação agora é da classe resultado_exame.py

4. UC 09. Importar dados de equipamentos laboratoriais

- Simulei 2 arquivos de importação, o dados_exame.csv e o dados_exame.json.
- As classes filhas importador_csv.py e importador_json.py leem o arquivo usando libs específicas
- A importação é tem uma relação de composição com uma instância de exame, através do método importar.

```python
    def importar(self, caminho_arquivo: str, exame):
```

5. UC 06. Disponibilizar laudos e resultados de exames

- Tem um gatilho automático no método liberar_resultado que instancia a notificacao sempre que um resultado é liberado.
- Para liberar um resultado, preciso obrigatoriamente ter um paciente e um resultado_exame
