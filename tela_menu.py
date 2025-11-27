import tkinter as tk

# Paleta de cores
COR_FUNDO = "#D0E6F7"  # azul suave
COR_TEXTO = "#333333"
COR_BOTAO = "#1E90FF"
COR_BOTAO_HOVER = "#2ECC71"
COR_ICONO = "#FFFFFF"

# Funções dos botões
def agendar():
    print("Agendar Consulta")

def cancelar():
    print("Cancelar Consulta")

def reagendar():
    print("Reagendar Consulta")

def minha_agenda():
    print("Minha Agenda")

def on_enter(event):
    event.widget.configure(bg=COR_BOTAO_HOVER)

def on_leave(event):
    event.widget.configure(bg=COR_BOTAO)

# Janela principal
root = tk.Tk()
root.title("Consult+ | Principal")
root.configure(bg=COR_FUNDO)
root.resizable(False, False)

# Tamanho e centralização
largura, altura = 420, 600
x = (root.winfo_screenwidth() // 2) - (largura // 2)
y = (root.winfo_screenheight() // 2) - (altura // 2)
root.geometry(f"{largura}x{altura}+{x}+{y}")

# Topo: logo + avatar
top_frame = tk.Frame(root, bg=COR_FUNDO)
top_frame.pack(fill="x", pady=(20, 10), padx=20)

# Logo em Canvas
canvas = tk.Canvas(top_frame, width=100, height=100, bg=COR_FUNDO, highlightthickness=0)
canvas.pack(side="left")
canvas.create_oval(20, 20, 55, 55, fill=COR_BOTAO, outline=COR_BOTAO)
canvas.create_oval(40, 20, 75, 55, fill=COR_BOTAO, outline=COR_BOTAO)
canvas.create_polygon(20, 35, 75, 35, 47, 85, fill=COR_BOTAO, outline=COR_BOTAO)
canvas.create_line(32, 58, 42, 68, fill=COR_FUNDO, width=4)
canvas.create_line(42, 68, 65, 45, fill=COR_FUNDO, width=4)
canvas.create_text(70, 25, text="+", font=("Arial", 16, "bold"), fill=COR_ICONO)

# Avatar (simulado como círculo)
avatar = tk.Canvas(top_frame, width=50, height=50, bg=COR_FUNDO, highlightthickness=0)
avatar.pack(side="right")
avatar.create_oval(5, 5, 45, 45, fill="#AAAAAA", outline="#AAAAAA")
avatar.create_text(25, 25, text="👤", font=("Arial", 18))

# Título
tk.Label(root, text="Consult+", font=("Arial Black", 24), bg=COR_FUNDO, fg=COR_TEXTO).pack(pady=(0, 30))

# Função para criar botões com ícones simulados
def criar_botao(texto, emoji, comando):
    btn = tk.Button(
        root, text=f"{emoji}  {texto}",
        font=("Arial", 12, "bold"),
        bg=COR_BOTAO, fg="white",
        activebackground=COR_BOTAO, activeforeground="white",
        relief="flat", bd=0,
        height=2, width=30,
        command=comando
    )
    btn.pack(pady=8)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Botões principais
criar_botao("Agendar Consulta", "📅", agendar)
criar_botao("Cancelar Consulta", "❌", cancelar)
criar_botao("Reagendar Consulta", "🔄", reagendar)
criar_botao("Minha Agenda", "🗓️", minha_agenda)

root.mainloop()