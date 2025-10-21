from utils.usuario import Usuario

class ModelLogin:
    def __init__(self):
        # Mockup do Banco de Dados
        self.usuarios = [
            Usuario(1, "ana", "1234", "Ana Souza", "ana@email.com", "9999-9999", "12/12/2012", "paciente"),
            Usuario(2, "carlos", "abcd", "Carlos Lima", "carlos@email.com", "9888-8888", "12/12/2012", "medico"),
            Usuario(3, "marina", "12345", "Marina Silva", "marina@email.com", "9777-7777", "12/12/2012", "secretaria"),
            Usuario(4, "joao", "4321", "João Pereira", "joao@email.com", "9666-6666", "12/12/2012", "tecnico")
        ]

    def confereDados(self, login, senha):
        for user in self.usuarios:
            if user.login == login and user.senha == senha:
                return True
        return False

    def retornaUser(self, login):
        for user in self.usuarios:
            if user.login == login:
                return user
        return None