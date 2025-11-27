import tkinter as tk

# Paleta de cores
COR_FUNDO = "#F5F5F5"
COR_AZUL_CLARO = "#4DB6E5"
COR_AZUL_ESCURO = "#1E90FF"
COR_TEXTO = "#333333"
COR_BOTAO = "#1E90FF"
COR_BOTAO_HOVER = "#2ECC71"

# Funções
def on_enter(event):
    event.widget.configure(bg=COR_BOTAO_HOVER)

def on_leave(event):
    event.widget.configure(bg=COR_BOTAO)

def abrir_cadastro():
    print("Abrir tela de cadastro")

def abrir_login():
    print("Abrir tela de login")

# Janela principal
root = tk.Tk()
root.title("Consult+ | Bem-vindo")
root.configure(bg=COR_FUNDO)
root.resizable(False, False)

# Tamanho e centralização
largura, altura = 400, 500
x = (root.winfo_screenwidth() // 2) - (largura // 2)
y = (root.winfo_screenheight() // 2) - (altura // 2)
root.geometry(f"{largura}x{altura}+{x}+{y}")

# Logo em Canvas
canvas = tk.Canvas(root, width=120, height=120, bg=COR_FUNDO, highlightthickness=0)
canvas.pack(pady=(40, 10))
canvas.create_oval(30, 25, 65, 60, fill=COR_AZUL_CLARO, outline=COR_AZUL_CLARO)
canvas.create_oval(55, 25, 90, 60, fill=COR_AZUL_CLARO, outline=COR_AZUL_CLARO)
canvas.create_polygon(30, 45, 90, 45, 60, 95, fill=COR_AZUL_CLARO, outline=COR_AZUL_CLARO)
canvas.create_line(42, 62, 52, 72, fill=COR_FUNDO, width=4, capstyle=tk.ROUND)
canvas.create_line(52, 72, 78, 50, fill=COR_FUNDO, width=4, capstyle=tk.ROUND)
canvas.create_text(86, 28, text="+", font=("Arial", 18, "bold"), fill=COR_AZUL_ESCURO)

# Título Consult+
tk.Label(root, text="Consult+", font=("Arial Black", 24, "italic"), bg=COR_FUNDO, fg=COR_TEXTO).pack(pady=(0, 40))

# Botão Cadastrar
btn_cadastrar = tk.Button(
    root, text="Cadastrar",
    font=("Arial", 12, "bold"),
    bg=COR_BOTAO, fg="white",
    activebackground=COR_BOTAO, activeforeground="white",
    relief="flat", bd=0,
    height=2, width=20,
    command=abrir_cadastro
)
btn_cadastrar.pack(pady=10)
btn_cadastrar.bind("<Enter>", on_enter)
btn_cadastrar.bind("<Leave>", on_leave)

# Botão Login
btn_login = tk.Button(
    root, text="Login",
    font=("Arial", 12, "bold"),
    bg=COR_BOTAO, fg="white",
    activebackground=COR_BOTAO, activeforeground="white",
    relief="flat", bd=0,
    height=2, width=20,
    command=abrir_login
)
btn_login.pack(pady=10)
btn_login.bind("<Enter>", on_enter)
btn_login.bind("<Leave>", on_leave)

root.mainloop()