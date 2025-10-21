class ViewLogin:
    def __init__(self, controller):
        self.controller = controller

    def informarLoginSenha(self):
        while True:
            login = input("Digite o login: ")
            senha = input("Digite a senha: ")
            user = self.controller.pegaLoginSenha(login, senha)

            if user:
                self.mostrarResultado(user)
                break  # login correto quebra o loop
            else:
                # Se não quebrar pergunta o que ele quer fazer
                print("\nLogin ou senha incorretos.")
                print("1. Tentar novamente")
                print("2. Solicitar auxílio da secretaria")
                escolha = input("Escolha uma opção (1 ou 2): ")
                if escolha == "2":
                    self.controller.notificarSecretaria(login)
                    print("""A secretaria já foi notificada da sua tentativa de Login
Para mais detalhes, entre em contato via secretaria@gmail.com""")
                    break  # não tenta mais depois de entrar em contato com a secretaria

    def mostrarResultado(self, user):
        if user:
            print(f"\nBem-vindo, {user.nome_completo}!")
            print(f"Tipo de usuário: {user.tipo.capitalize()}")
            print(f"E-mail: {user.email}")
            print(f"Telefone: {user.telefone}")

            # Por enquanto as ações específicas de cada classe são só um print mesmo
            if user.tipo == "paciente":
                print("""→ Exportar exames.""")
            elif user.tipo == "medico":
                print("""→ Agendar exames.
→ Agendar procedimentos.
→ Disponibilizar laudos e resultados de exames.
→ Realizar encaminhamentos.
→ Acessar estatísticas gerenciais""")
            elif user.tipo == "tecnico":
                print("""→ Agendar exames.
→ Agendar procedimentos.
→ Disponibilizar laudos e resultados de exames.
→ Importar dados de equipamentos laboratoriais
→ Acessar estatísticas gerenciais""")
            elif user.tipo == "secretaria":
                print("""→ Gerenciar pacientes
→ Gerenciar usuários
→ Acessar estatísticas gerenciais""")