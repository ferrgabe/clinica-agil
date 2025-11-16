import tkinter as tk
from tkinter import ttk, messagebox

from mvcpacientes.controllers.servico_pacientes import ServicoPacientes
from mvcpacientes.models.repositorio_pacientes import FabricaRepositorioPacientes
from mvcpacientes.controllers.estrategias_listagem import (
    ListarPorNome,
    ListarPorDataCadastro,
    ListarPorId,
)



def main():
    # Cria o repositório (troque para "memoria" se quiser testar sem DB)
    repositorio = FabricaRepositorioPacientes.criar_repositorio("postgres")
    servico = ServicoPacientes(repositorio)

    # Janela principal
    root = tk.Tk()
    root.title("Clínica Ágil - Módulo de Pacientes")
    root.geometry("700x550")  # largura x altura

    # Título da tela
    titulo = ttk.Label(
        root,
        text="Cadastro de Pacientes",
        font=("Arial", 16, "bold")
    )
    titulo.pack(pady=20)

    # Frame do formulário
    form_frame = ttk.Frame(root, padding=10)
    form_frame.pack(fill="x", padx=20, pady=10)

    # Dicionário para guardar os campos
    campos = {}

    # Estratégia selecionada na tela (para o Strategy)
    estrategia_var = tk.StringVar(value="Nome (A-Z)")

    def adicionar_campo(linha, rotulo, nome_campo, largura=40, show=None):
        label = ttk.Label(form_frame, text=rotulo)
        label.grid(row=linha, column=0, sticky="w", pady=5)

        entry = ttk.Entry(form_frame, width=largura, show=show)
        entry.grid(row=linha, column=1, sticky="w", pady=5)

        campos[nome_campo] = entry

    # Campos do formulário
    adicionar_campo(0, "Login:", "login")
    adicionar_campo(1, "Senha (apenas números):", "senha", show="*")
    adicionar_campo(2, "Nome completo:", "nome")
    adicionar_campo(3, "Email:", "email")
    adicionar_campo(4, "Telefone (apenas números):", "telefone")
    adicionar_campo(5, "CPF (somente números):", "cpf")
    adicionar_campo(6, "Data de nascimento (DD/MM/AAAA):", "data_nascimento")
    adicionar_campo(7, "Tipo (ex: paciente):", "tipo")

    # Seletor de estratégia de listagem (Strategy)
    frame_estrategia = ttk.Frame(root, padding=10)
    frame_estrategia.pack(fill="x", padx=20, pady=5)

    lbl_estrategia = ttk.Label(frame_estrategia, text="Ordenar por:")
    lbl_estrategia.pack(side="left")

    combo_estrategia = ttk.Combobox(
        frame_estrategia,
        textvariable=estrategia_var,
        state="readonly",
        values=[
            "Nome (A-Z)",
            "Data de cadastro",
            "ID"
        ]
    )
    combo_estrategia.pack(side="left", padx=10)
    combo_estrategia.current(0)

    def on_cadastrar():
        # Coleta os dados da tela
        dados = {nome: campo.get().strip() for nome, campo in campos.items()}

        login = dados["login"]
        senha_str = dados["senha"]
        nome = dados["nome"]
        email = dados["email"]
        telefone_str = dados["telefone"]
        cpf = dados["cpf"]
        data_nascimento = dados["data_nascimento"]
        tipo = dados["tipo"] or "paciente"

        # Validações básicas de preenchimento
        if not login or not nome or not email or not cpf or not data_nascimento:
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
            return

        # Validação numérica
        if not senha_str.isdigit():
            messagebox.showerror("Erro", "A senha deve conter apenas números.")
            return

        if not telefone_str.isdigit():
            messagebox.showerror("Erro", "O telefone deve conter apenas números.")
            return

        if not cpf.isdigit() or len(cpf) != 11:
            messagebox.showerror("Erro", "CPF deve conter 11 dígitos numéricos.")
            return

        try:
            servico.cadastrar(
                login=login,
                senha=int(senha_str),
                nome=nome,
                email=email,
                telefone=int(telefone_str),
                cpf=cpf,
                data_nascimento=data_nascimento,
                tipo=tipo,
            )
            messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")

            # Limpar campos após cadastro
            for campo in campos.values():
                campo.delete(0, tk.END)

        except ValueError as e:
            # Erros de validação do serviço (CPF, data inválida, etc.)
            messagebox.showerror("Erro ao cadastrar", str(e))
        except Exception as e:
            # Qualquer erro inesperado (ex: problema de conexão com o banco)
            messagebox.showerror(
                "Erro inesperado",
                f"Não foi possível cadastrar o paciente.\n\nDetalhes: {e}"
            )

    def on_listar():
        # Define a estratégia com base na seleção do ComboBox
        valor = estrategia_var.get()

        if valor == "Nome (A-Z)":
            servico.definir_estrategia_listagem(ListarPorNome())
        elif valor == "Data de cadastro":
            servico.definir_estrategia_listagem(ListarPorDataCadastro())
        elif valor == "ID":
            servico.definir_estrategia_listagem(ListarPorId())

        try:
            pacientes = servico.listar()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível carregar os pacientes.\n\nDetalhes: {e}")
            return

        if not pacientes:
            messagebox.showinfo("Pacientes", "Nenhum paciente cadastrado.")
            return

        # Nova janela para exibir a lista
        janela = tk.Toplevel(root)
        janela.title("Pacientes cadastrados")
        janela.geometry("900x300")

        colunas = ("ID", "Login", "Nome", "Email", "Telefone", "Data Cadastro", "CPF", "Nascimento", "Tipo")

        tree = ttk.Treeview(janela, columns=colunas, show="headings")

        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="w")

        for p in pacientes:
            tree.insert(
                "",
                "end",
                values=(
                    p.idusuario,
                    p.login,
                    p.nome_completo,
                    p.email,
                    p.telefone,
                    p.data_cadastro,
                    p.cpf,
                    p.data_nascimento,
                    p.tipo,
                )
            )

        tree.pack(fill="both", expand=True)

    # Botões
    botoes_frame = ttk.Frame(root, padding=10)
    botoes_frame.pack(fill="x", padx=20, pady=10)

    btn_cadastrar = ttk.Button(botoes_frame, text="Cadastrar", command=on_cadastrar)
    btn_cadastrar.pack(side="left")

    btn_listar = ttk.Button(botoes_frame, text="Listar pacientes", command=on_listar)
    btn_listar.pack(side="left", padx=10)

    btn_fechar = ttk.Button(botoes_frame, text="Fechar", command=root.destroy)
    btn_fechar.pack(side="right")

    # Rodapé simples
    rodape = ttk.Label(
        root,
        text="Protótipo de interface - Módulo de Pacientes (Engenharia de Software)",
        font=("Arial", 9)
    )
    rodape.pack(side="bottom", pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
