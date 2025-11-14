class ControllerLogin:
    def __init__(self, model):
        self.model = model

    def pegaLoginSenha(self, login, senha):
        print("[Controller] Recebendo dados de login e senha...")
        return self.efetuaLogin(login, senha)

    def efetuaLogin(self, login, senha):
        print("[Controller] Verificando com o Model...")
        if self.model.confereDados(login, senha):
            user = self.model.retornaUser(login)
            print(f"[Controller] Login bem-sucedido. Usuário: {user.nome_completo} ({user.tipo})")
            return user
        else:
            return None

    def notificarSecretaria(self, login):
        # Registra no log ou enviar e-mail depois?
        # Novamente por enquanto são só prints
        print(f"[Controller] O usuário com login '{login}' solicitou ajuda da secretaria.")
        print("[Controller] Secretaria notificada para entrar em contato.")
