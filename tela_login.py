import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Paleta de cores
COR_FUNDO = "#F5F5F5"
COR_AZUL_CLARO = "#4DB6E5"   # azul claro para o coração
COR_AZUL_ESCURO = "#1E90FF"  # azul escuro para o "+"
COR_TEXTO = "#333333"
COR_BOTAO = "#1E90FF"
COR_BOTAO_HOVER = "#2ECC71"  # verde ao passar o mouse

# Funções
def login():
    nome = entry_nome.get()
    senha = entry_senha.get()
    if nome and senha and nome != "Nome" and senha != "Senha":
        messagebox.showinfo("Login", f"Bem-vindo, {nome}!")
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos corretamente.")

def abrir_cadastro(event=None):
    print("Abrir Cadastro")

def limpar_placeholder(event, campo, texto):
    if campo.get() == texto:
        campo.delete(0, tk.END)

def restaurar_placeholder(event, campo, texto):
    if campo.get() == "":
        campo.insert(0, texto)

def on_btn_enter(event):
    btn_entrar.configure(bg=COR_BOTAO_HOVER, activebackground=COR_BOTAO_HOVER)

def on_btn_leave(event):
    btn_entrar.configure(bg=COR_BOTAO, activebackground=COR_BOTAO)

# Janela principal
root = tk.Tk()
root.title("Consult+ | Login")
root.configure(bg=COR_FUNDO)
root.resizable(False, False)

# Tamanho e centralização
largura, altura = 400, 550
x = (root.winfo_screenwidth() // 2) - (largura // 2)
y = (root.winfo_screenheight() // 2) - (altura // 2)
root.geometry(f"{largura}x{altura}+{x}+{y}")

# Logo em Canvas: coração + check + "+"
canvas = tk.Canvas(root, width=120, height=120, bg=COR_FUNDO, highlightthickness=0)
canvas.pack(pady=(30, 10))

# Desenho do coração (duas circunferências + polígono)
# Coordenadas base para um coração suave e centrado
# Dois círculos no topo
canvas.create_oval(30, 25, 65, 60, fill=COR_AZUL_CLARO, outline=COR_AZUL_CLARO)
canvas.create_oval(55, 25, 90, 60, fill=COR_AZUL_CLARO, outline=COR_AZUL_CLARO)
# Triângulo/bulbo inferior para formar a ponta
canvas.create_polygon(
    30, 45,   # esquerda topo
    90, 45,   # direita topo
    60, 95,   # ponta inferior
    fill=COR_AZUL_CLARO, outline=COR_AZUL_CLARO
)

# Check (na cor do fundo, para simular recorte sobre o coração)
canvas.create_line(42, 62, 52, 72, fill=COR_FUNDO, width=4, capstyle=tk.ROUND)
canvas.create_line(52, 72, 78, 50, fill=COR_FUNDO, width=4, capstyle=tk.ROUND)

# Sinal de + no canto superior direito do coração
canvas.create_text(86, 28, text="+", font=("Arial", 18, "bold"), fill=COR_AZUL_ESCURO)

# Título/Logo textual
tk.Label(root, text="Consult+", font=("Arial Black", 24), bg=COR_FUNDO, fg=COR_TEXTO).pack(pady=(0, 30))

# Estilo ttk para entradas (visual limpo)
style = ttk.Style()
style.theme_use("clam")
style.configure("Rounded.TEntry", padding=10, relief="flat", borderwidth=0)
style.map("Rounded.TEntry",
          fieldbackground=[("!disabled", "#EAF6FD")],  # leve azul/cinza
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

# Campo Senha
frame_senha = tk.Frame(root, bg=COR_FUNDO)
frame_senha.pack(pady=(0, 20), padx=40, fill="x")
tk.Label(frame_senha, text="Senha", font=("Arial", 11), bg=COR_FUNDO, fg=COR_TEXTO, anchor="w").pack(fill="x")
entry_senha = ttk.Entry(frame_senha, style="Rounded.TEntry", font=("Arial", 12), show="*")
entry_senha.insert(0, "Senha")
entry_senha.pack(fill="x", ipady=8)
entry_senha.bind("<FocusIn>", lambda e: limpar_placeholder(e, entry_senha, "Senha"))
entry_senha.bind("<FocusOut>", lambda e: restaurar_placeholder(e, entry_senha, "Senha"))

# Botão ENTRAR com hover verde
btn_entrar = tk.Button(
    root, text="ENTRAR",
    font=("Arial", 12, "bold"),
    bg=COR_BOTAO, fg="white",
    activebackground=COR_BOTAO, activeforeground="white",
    relief="flat", bd=0,
    height=2, width=22,
    command=login
)
btn_entrar.pack(pady=10)
btn_entrar.bind("<Enter>", on_btn_enter)
btn_entrar.bind("<Leave>", on_btn_leave)

# Link de cadastro
frame_cadastro = tk.Frame(root, bg=COR_FUNDO)
frame_cadastro.pack(pady=30)
tk.Label(frame_cadastro, text="Não possui cadastro?", font=("Arial", 10), bg=COR_FUNDO, fg=COR_TEXTO).pack()
link = tk.Label(frame_cadastro, text="CADASTRAR-SE", font=("Arial", 10, "underline"),
                fg=COR_AZUL_ESCURO, bg=COR_FUNDO, cursor="hand2")
link.pack()
link.bind("<Button-1>", abrir_cadastro)

# Foco inicial e ordem de Tab
entry_nome.focus_set()
entry_nome.tk_focusNext = entry_senha
entry_senha.tk_focusNext = btn_entrar

root.mainloop()