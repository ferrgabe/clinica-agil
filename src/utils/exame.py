class Exame:
    def __init__(self, nome, data, resultado):
        self.nome = nome
        self.data = data
        self.resultado = resultado

    def __str__(self):
        return f"Exame(nome='{self.nome}', data='{self.data}', resultado='{self.resultado}')"

    def __repr__(self):
        return self.__str__()
