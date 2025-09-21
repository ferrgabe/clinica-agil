from datetime import date

class Usuario:
    def __init__(
        self,
        idusuario: int,
        login: str,
        senha: int,
        nome_completo: str,
        email: str,
        telefone: int,
        data_cadastro: date,
    ):
        self.idusuario = idusuario
        self.login = login
        self.senha = senha
        self.nome_completo = nome_completo
        self.email = email
        self.telefone = telefone
        self.data_cadastro = data_cadastro

    @staticmethod
    def login(lista_usuarios, login_informado: str, senha_informada: int):
        """
        To aproveitando um pedaço de código de outro trabalho meu que fazia algo parecido.
        A ideia é a gente tenha uma função genérica de login que saiba dizer qual classe de usuário
        está logando, e aí a gente pode usar isso pra dizer quais funções devem ser acessíveis.
        """
        for usuario in lista_usuarios:
            if usuario.login == login_informado or usuario.email == login_informado:
                if usuario.senha == senha_informada:
                    return True, f"Login realizado! Bem-vindo, {usuario.nome_completo} ({usuario.__class__.__name__}).", usuario
                else:
                    return False, "Senha incorreta.", None
        return False, "Usuário ou email não encontrado.", None
