import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Paleta de cores
COR_FUNDO = "#F5F5F5"
COR_AZUL_CLARO = "#4DB6E5"
COR_AZUL_ESCURO = "#1E90FF"
COR_TEXTO = "#333333"
COR_BOTAO = "#1E90FF"
COR_BOTAO_HOVER = "#2ECC71"
COR_SOCIAL_TEXTO = "#FF8C00"

# Cores de marcas
COR_GOOGLE = "#DB4437"
COR_FACEBOOK = "#3B5998"
COR_APPLE = "#000000"

# Funções principais
def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()
    if all([nome, email, senha]) and nome != "Nome" and email != "Email" and senha != "Senha":
        messagebox.showinfo("Cadastro", f"Cadastro realizado com sucesso para {nome}!")
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos corretamente.")

def limpar_placeholder(event, campo, texto):
    if campo.get() == texto:
        campo.delete(0, tk.END)

def restaurar_placeholder(event, campo, texto):
    if campo.get() == "":
        campo.insert(0, texto)

def on_btn_enter(event):
    btn_cadastrar.configure(bg=COR_BOTAO_HOVER, activebackground=COR_BOTAO_HOVER)

def on_btn_leave(event):
    btn_cadastrar.configure(bg=COR_BOTAO, activebackground=COR_BOTAO)

# Ícones sociais (Canvas redondo com hover)
def criar_icone_social(parent, nome, cor_base, texto, comando_click):
    w, h = 54, 54
    c = tk.Canvas(parent, width=w, height=h, bg=COR_FUNDO, highlightthickness=0, cursor="hand2")
    c.pack(side="left", padx=8)

    # círculo
    circle = c.create_oval(4, 4, w-4, h-4, fill=cor_base, outline=cor_base)
    label = c.create_text(w//2, h//2, text=texto, fill="white", font=("Arial", 16, "bold"))

    def hover_in(_):
        c.itemconfig(circle, fill=ajustar_brilho(cor_base, 1.15), outline=ajustar_brilho(cor_base, 1.15))
    def hover_out(_):
        c.itemconfig(circle, fill=cor_base, outline=cor_base)
    def on_click(_):
        print(f"Login social: {nome}")

    c.bind("<Enter>", hover_in)
    c.bind("<Leave>", hover_out)
    c.bind("<Button-1>", on_click)
    # também permitir clicar no texto
    c.tag_bind(label, "<Enter>", hover_in)
    c.tag_bind(label, "<Leave>", hover_out)
    c.tag_bind(label, "<Button-1>", on_click)

    return c

def ajustar_brilho(hex_cor, fator):
    # hex_cor "#RRGGBB" -> ajusta brilho multiplicando por fator
    hex_cor = hex_cor.lstrip("#")
    r = max(0, min(255, int(int(hex_cor[0:2], 16) * fator)))
    g = max(0, min(255, int(int(hex_cor[2:4], 16) * fator)))
    b = max(0, min(255, int(int(hex_cor[4:6], 16) * fator)))
    return f"#{r:02X}{g:02X}{b:02X}"

# Janela principal
root = tk.Tk()
root.title("Consult+ | Cadastro")
root.configure(bg=COR_FUNDO)
root.resizable(False, False)

# Tamanho e centralização
largura, altura = 400, 600
x = (root.winfo_screenwidth() // 2) - (largura // 2)
y = (root.winfo_screenheight() // 2) - (altura // 2)
root.geometry(f"{largura}x{altura}+{x}+{y}")

# Logo em Canvas (coração + check + "+")
canvas = tk.Canvas(root, width=120, height=120, bg=COR_FUNDO, highlightthickness=0)
canvas.pack(pady=(30, 10))
canvas.create_oval(30, 25, 65, 60, fill=COR_AZUL_CLARO, outline=COR_AZUL_CLARO)
canvas.create_oval(55, 25, 90, 60, fill=COR_AZUL_CLARO, outline=COR_AZUL_CLARO)
canvas.create_polygon(30, 45, 90, 45, 60, 95, fill=COR_AZUL_CLARO, outline=COR_AZUL_CLARO)
canvas.create_line(42, 62, 52, 72, fill=COR_FUNDO, width=4, capstyle=tk.ROUND)
canvas.create_line(52, 72, 78, 50, fill=COR_FUNDO, width=4, capstyle=tk.ROUND)
canvas.create_text(86, 28, text="+", font=("Arial", 18, "bold"), fill=COR_AZUL_ESCURO)

# Título textual
tk.Label(root, text="Consult+", font=("Arial Black", 24), bg=COR_FUNDO, fg=COR_TEXTO).pack(pady=(0, 20))

# Estilo ttk
style = ttk.Style()
style.theme_use("clam")
style.configure("Rounded.TEntry", padding=10, relief="flat", borderwidth=0)
style.map("Rounded.TEntry",
          fieldbackground=[("!disabled", "#EAF6FD")],
          foreground=[("!disabled", "#000")])

# Campo Nome
frame_nome = tk.Frame(root, bg=COR_FUNDO)
frame_nome.pack(pady=(0, 10), padx=40, fill="x")
tk.Label(frame_nome, text="Nome", font=("Arial", 11), bg=COR_FUNDO, fg=COR_TEXTO, anchor="w").pack(fill="x")
entry_nome = ttk.Entry(frame_nome, style="Rounded.TEntry", font=("Arial", 12))
entry_nome.insert(0, "Nome")
entry_nome.pack(fill="x", ipady=8)
entry_nome.bind("<FocusIn>", lambda e: limpar_placeholder(e, entry_nome, "Nome"))
entry_nome.bind("<FocusOut>", lambda e: restaurar_placeholder(e, entry_nome, "Nome"))

# Campo Email
frame_email = tk.Frame(root, bg=COR_FUNDO)
frame_email.pack(pady=(0, 10), padx=40, fill="x")
tk.Label(frame_email, text="Email", font=("Arial", 11), bg=COR_FUNDO, fg=COR_TEXTO, anchor="w").pack(fill="x")
entry_email = ttk.Entry(frame_email, style="Rounded.TEntry", font=("Arial", 12))
entry_email.insert(0, "Email")
entry_email.pack(fill="x", ipady=8)
entry_email.bind("<FocusIn>", lambda e: limpar_placeholder(e, entry_email, "Email"))
entry_email.bind("<FocusOut>", lambda e: restaurar_placeholder(e, entry_email, "Email"))

# Campo Senha
frame_senha = tk.Frame(root, bg=COR_FUNDO)
frame_senha.pack(pady=(0, 20), padx=40, fill="x")
tk.Label(frame_senha, text="Senha", font=("Arial", 11), bg=COR_FUNDO, fg=COR_TEXTO, anchor="w").pack(fill="x")
entry_senha = ttk.Entry(frame_senha, style="Rounded.TEntry", font=("Arial", 12), show="*")
entry_senha.insert(0, "Senha")
entry_senha.pack(fill="x", ipady=8)
entry_senha.bind("<FocusIn>", lambda e: limpar_placeholder(e, entry_senha, "Senha"))
entry_senha.bind("<FocusOut>", lambda e: restaurar_placeholder(e, entry_senha, "Senha"))

# Botão Cadastrar com hover verde
btn_cadastrar = tk.Button(
    root, text="Cadastrar",
    font=("Arial", 12, "bold"),
    bg=COR_BOTAO, fg="white",
    activebackground=COR_BOTAO, activeforeground="white",
    relief="flat", bd=0,
    height=2, width=22,
    command=cadastrar
)
btn_cadastrar.pack(pady=10)
btn_cadastrar.bind("<Enter>", on_btn_enter)
btn_cadastrar.bind("<Leave>", on_btn_leave)

# Texto redes sociais
tk.Label(root, text="conecte-se com suas redes sociais",
         font=("Arial", 10), bg=COR_FUNDO, fg=COR_SOCIAL_TEXTO).pack(pady=(20, 10))

# Ícones das redes sociais (Google, Facebook, Apple)
frame_icons = tk.Frame(root, bg=COR_FUNDO)
frame_icons.pack()

criar_icone_social(frame_icons, "Google", COR_GOOGLE, "G", comando_click=lambda: print("Google"))
criar_icone_social(frame_icons, "Facebook", COR_FACEBOOK, "f", comando_click=lambda: print("Facebook"))
criar_icone_social(frame_icons, "Apple", COR_APPLE, "", comando_click=lambda: print("Apple"))

# Foco inicial
entry_nome.focus_set()

root.mainloop()